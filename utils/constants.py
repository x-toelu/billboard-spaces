MONTHS_IN_YEAR = 12
WEEKS_IN_MONTH = 4

NIGERIAN_STATES = [
    ('abia', 'Abia'), ('adamawa', 'Adamawa'), ('akwa_ibom', 'Akwa Ibom'),
    ('anambra', 'Anambra'), ('bauchi', 'Bauchi'), ('bayelsa', 'Bayelsa'),
    ('benue', 'Benue'), ('borno', 'Borno'), ('cross_river', 'Cross River'),
    ('delta', 'Delta'), ('ebonyi', 'Ebonyi'), ('edo', 'Edo'), ('ekiti', 'Ekiti'),
    ('enugu', 'Enugu'), ('gombe', 'Gombe'), ('imo', 'Imo'), ('jigawa', 'Jigawa'),
    ('kaduna', 'Kaduna'), ('kano', 'Kano'), ('katsina', 'Katsina'),
    ('kebbi', 'Kebbi'), ('kogi', 'Kogi'), ('kwara', 'Kwara'), ('lagos', 'Lagos'),
    ('nasarawa', 'Nasarawa'), ('niger', 'Niger'), ('ogun', 'Ogun'),
    ('ondo', 'Ondo'), ('osun', 'Osun'), ('oyo', 'Oyo'), ('plateau', 'Plateau'),
    ('rivers', 'Rivers'), ('sokoto', 'Sokoto'), ('taraba', 'Taraba'),
    ('yobe', 'Yobe'), ('zamfara', 'Zamfara'), ('fct_abuja', 'FCT (Abuja)')
]


USER_CHOICES = (
    ('billboard_owner', 'Billboard Owner'),
    ('state_agent', 'State Agent'),
    ('advertising_agent', 'Advertising Agent'),
    ('business_owner', 'Business Owner'),
)


SUBSCRIBERS_FEATURES = {
    'free': {
        'max_billboards_upload': 3,
        'max_billboards_sale': 2,
        'analytics': False,
    },

    'basic': {
        'max_billboards_upload': 5,
        'max_billboards_sale': 3,
        'analytics': False,
    },

    'pro': {
        'max_billboards_upload': float('inf'),
        'max_billboards_sale': float('inf'),
        'analytics': True,
    }
}
