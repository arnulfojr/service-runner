import os


USERNAME = os.getenv('GIT_USERNAME')

PASSWORD = os.getenv('GIT_PASSWORD')


def build_git(endpoint: str,
              user: str = USERNAME,
              password: str = PASSWORD,
              protocol: str = 'https'):
    if ':77' in endpoint:
        protocol, endpoint = endpoint.split('://')
    return f'{protocol}://{user}:{password}@{endpoint}'
