# tests/utils/drupal_api.py
import copy
import json
from pathlib import Path
import requests


class DrupalAPIUtils:
    def __init__(self, base_url: str, username: str, password: str, payload_config_path=None):
        """
        base_url: Drupal domain, e.g. https://example.com
        username/password: API user
        """
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password

        # Use session for performance
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.session.headers.update({
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json",
        })

        # Load payload templates from JSON
        if payload_config_path is None:
            # default: tests/data/drupal_payloads.json (adjust to your layout)
            payload_config_path = Path(__file__).parent.parent / "data" / "drupal_payloads.json"
        else:
            payload_config_path = Path(payload_config_path)

        with payload_config_path.open("r", encoding="utf-8") as f:
            self.payload_templates = json.load(f)


    # ------------------------------------------------------------------
    # Payload Builder
    # ------------------------------------------------------------------

    def build_payload(self, content_type: str) -> dict:
        """
        Build a JSON:API payload based on a template from drupal_payloads.json.
        """
        if content_type not in self.payload_templates:
            raise ValueError(f"No payload template defined for content_type '{content_type}'")

        # Deep copy so we don't mutate the template in memory
        template = copy.deepcopy(self.payload_templates[content_type])

        # data = template["data"]
        # attrs = data.setdefault("attributes", {})
        #
        # # Ensure "type" matches the content type (you can trust JSON, or enforce)
        # data["type"] = data.get("type", f"node--{content_type}")

        # Fill in dynamic fields
        # attrs["title"] = title

        # body_field_name = attrs.get("field_body")  # our helper key
        # if body_field_name:
        #     # Ensure field exists
        #     # field_def = attrs.setdefault(body_field_name, {})
        #     # field_def["value"] = body_html
        #     # field_def.setdefault("format", "basic_html")
        #     # We don't want to send "body_field" to Drupal
        #     attrs.pop("body_field", None)

        return template

    # ---------- CRUD wrappers ----------

    # ------------------------------------------------------------------
    # Create a node
    # ------------------------------------------------------------------

    def create_node(self, content_type: str) -> dict:
        url = f"{self.base_url}/jsonapi/node/{content_type}"
        payload = self.build_payload(content_type)

        resp = self.session.post(url, json=payload)
        if resp.status_code >= 400:
            print("\n[DRUPAL DEBUG CREATE]", resp.status_code)
            print(resp.text)
        resp.raise_for_status()
        return resp.json()

    # ------------------------------------------------------------------
    # Delete a node by UUID
    # ------------------------------------------------------------------
    def delete_node(self, content_type: str, node_uuid: str):
        url = f"{self.base_url}/jsonapi/node/{content_type}/{node_uuid}"

        response = self.session.delete(url)
        # 204 No Content is expected
        if response.status_code not in (200, 202, 204):
            raise Exception(f"Delete failed: {response.status_code} - {response.text}")

        return True

    # ------------------------------------------------------------------
    # Find nodes by title
    # ------------------------------------------------------------------
    def find_nodes_by_title(self, content_type: str, title: str):
        url = (
            f"{self.base_url}/jsonapi/node/{content_type}"
            f"?filter[title][value]={title}&filter[title][operator]=="
        )

        response = self.session.get(url)
        response.raise_for_status()
        return response.json().get("data", [])

    # ------------------------------------------------------------------
    # Create then return UUID only
    # ------------------------------------------------------------------
    def create_node_and_get_uuid(self, content_type: str, title: str, body_html: str):
        node = self.create_node(content_type)
        return node["data"]["id"]


