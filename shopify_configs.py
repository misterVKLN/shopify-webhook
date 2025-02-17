from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env-features",
        """
"ENABLE_BULK_ENROLLMENT_VIEW": true
"""
    )
)


hooks.Filters.ENV_PATCHES.add_items([
    ("openedx-lms-common-settings", """
WEBHOOK_RECEIVER_EDX_OAUTH2_KEY = "webhook_receiver"
WEBHOOK_RECEIVER_EDX_OAUTH2_SECRET = "REPLACE"
WEBHOOK_RECEIVER_SEND_ENROLLMENT_EMAIL = True
WEBHOOK_RECEIVER_AUTO_ENROLL = True
WEBHOOK_RECEIVER_SETTINGS = {
    'shopify': {
        'shop_domain': '6dc7d5-5.myshopify.com',
        'api_key': 'ec85be6e249080ca97d6a3337effdfe845caf82656a3b40724f612725942d257',
    }
}
SHOPIFY_ADMIN_API_URL = "https://6dc7d5-5.myshopify.com/admin/api/2024-10/graphql.json"
SHOPIFY_ADMIN_API_ACCESS_TOKEN = "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"
    """)
])
