#: JSON schema to validate virtual gallery data source
GALLERY_DATA_SCHEMA = {
    "name": "Data source for Virtual 3D gallery",
    "type": "object",
    "properties": {
        "images": {
            "name": "Images to display in the Virtual Gallery",
            "type": "array",
            "items": {
               "name": "Image",
               "type": "object",
               "properties": {
                    "title": {
                        "type": "string",
                        "required": True,
                    },
                    "description": {
                        "type": "string",
                        "required": True,
                    },
                    "author": {
                        "type": "string",
                        "required": True,
                    },
                    "url": {
                        "type": "string",
                        "required": True,
                    },
                }
            }
        },
        "settings": {
            "name": "Virtual Gallery settings",
            "type": "object",
            "properties": {
                "anaglyphModeEnabled": {
                    "type": "string",
                    "title": "Is anaglyph mode enabled?",
                    "required": True,
                }
            }
        },
        "ui": {
            "name": "Virtual Gallery UI strings",
            "type": "object",
            "properties": {
                "anaglyph": {
                    "type": "string",
                    "required": True,
                },
                "fullscreen": {
                    "type": "string",
                    "required": True,
                },
                "loadingImg": {
                    "type": "string",
                    "required": True,
                },
                "enterRoom": {
                    "type": "string",
                    "required": True,
                },
                "enterRoomToolTip": {
                    "type": "string",
                    "required": True,
                },
            }
        }
    }
}
