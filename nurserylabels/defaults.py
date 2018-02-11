from mezzanine.conf import register_setting

register_setting(
    name="NURSERY_FRONT_LABEL_PATH",
    label="Nursery: Front Label Path",
    description="The path to where the front nursery label should be saved.",
    editable=True,
    default='',
)

register_setting(
    name="NURSERY_BACK_LABEL_PATH",
    label="Nursery: Back Label Path",
    description="The path to where the back nursery label should be saved.",
    editable=True,
    default='',
)

register_setting(
    name="NURSERY_BOX_LABEL_PATH",
    label="Nursery: Box Label Path",
    description="The path to where the box nursery label should be saved.",
    editable=True,
    default='',
)
