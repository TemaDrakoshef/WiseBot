from src.infrastructure.api.base import BaseClient
from src.infrastructure.api.wise.schemas import WiseId


class WiseAPI(BaseClient):
    def __init__(self, api_token: str, **kwargs):
        production_url = "https://api.transferwise.com"

        self.base_url = production_url
        self.headers = {
            'Authorization': f'Bearer {api_token}',
        }

        super().__init__(base_url=self.base_url, headers=self.headers)

    async def get_current_user(self):
        """
        Retrieve current user by token.
        :return: Response includes also personal user's profile info.
        """
        response = await self._make_request(
            "GET",
            "/v1/me"
        )

        return response[1]

    async def get_user_profiles(self):
        """
        List of all profiles belonging to user.
        :return: An array of profile objects will be returned.
        """
        response = await self._make_request(
            "GET",
            "/v2/profiles"
        )

        return response[1]

    async def get_list_balances(self, profile_id: WiseId):
        """
        List balances for a profile.
        :param profile_id: Authenticated profile id.
        :return: It returns all balance accounts the profile has in the types specified.
        """
        response = await self._make_request(
            "GET",
            f"/v4/profiles/{profile_id}/balances?types=STANDARD"
        )

        return response[1]
