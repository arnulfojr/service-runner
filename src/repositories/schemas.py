"""Configuration schema."""


CONFIG_SCHEMA = {
    'version': {
        'required': True,
        'type': 'string'
    },
    'git': {
        'required': True,
        'type': 'dict',
        'schema': {
            'user': {
                'required': True,
                'type': 'string'
            }
        }
    },
    'repositories': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'name': {
                    'type': 'string',
                    'required': True
                },
                'branch': {
                    'type': 'string',
                    'default': 'master'
                },
                'clone': {
                    'type': 'boolean',
                    'default': True
                }
            }
        }
    }
}
