# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TokenRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self,
                 grant_type: str=None,
                 client_id: str=None,
                 client_secret: str=None,
                 scope: str=None,
                 redirect_uri: str=None,
                 code: str=None,
                 code_verifier: str=None,
                 refresh_token: str=None):  # noqa: E501
        """TokenRequest - a model defined in Swagger

        :param grant_type: The grant_type of this TokenRequest.  # noqa: E501
        :type grant_type: str
        :param client_id: The client_id of this TokenRequest.  # noqa: E501
        :type client_id: str
        :param client_secret: The client_secret of this TokenRequest.  # noqa: E501
        :type client_secret: str
        :param scope: The scope of this TokenRequest.  # noqa: E501
        :type scope: str
        :param redirect_uri: The redirect_uri of this TokenRequest.  # noqa: E501
        :type redirect_uri: str
        :param code: The code of this TokenRequest.  # noqa: E501
        :type code: str
        :param code_verifier: The code_verifier of this TokenRequest.  # noqa: E501
        :type code_verifier: str
        :param refresh_token: The refresh_token of this TokenRequest.  # noqa: E501
        :type refresh_token: str
        """
        self.swagger_types = {
            'grant_type': str,
            'client_id': str,
            'client_secret': str,
            'scope': str,
            'redirect_uri': str,
            'code': str,
            'code_verifier': str,
            'refresh_token': str
        }

        self.attribute_map = {
            'grant_type': 'grant_type',
            'client_id': 'client_id',
            'client_secret': 'client_secret',
            'scope': 'scope',
            'redirect_uri': 'redirect_uri',
            'code': 'code',
            'code_verifier': 'code_verifier',
            'refresh_token': 'refresh_token'
        }
        self._grant_type = grant_type
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope
        self._redirect_uri = redirect_uri
        self._code = code
        self._code_verifier = code_verifier
        self._refresh_token = refresh_token

    @classmethod
    def from_dict(cls, dikt) -> 'TokenRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TokenRequest of this TokenRequest.  # noqa: E501
        :rtype: TokenRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grant_type(self) -> str:
        """Gets the grant_type of this TokenRequest.

        grant type of token. Valid values: [authorization_code, pkce, client_credentials, password, refresh].  # noqa: E501

        :return: The grant_type of this TokenRequest.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type: str):
        """Sets the grant_type of this TokenRequest.

        grant type of token. Valid values: [authorization_code, pkce, client_credentials, password, refresh].  # noqa: E501

        :param grant_type: The grant_type of this TokenRequest.
        :type grant_type: str
        """
        if grant_type is None:
            raise ValueError(
                "Invalid value for `grant_type`, must not be `None`")  # noqa: E501

        self._grant_type = grant_type

    @property
    def client_id(self) -> str:
        """Gets the client_id of this TokenRequest.

        client app identifier. Required for each grant type  # noqa: E501

        :return: The client_id of this TokenRequest.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Sets the client_id of this TokenRequest.

        client app identifier. Required for each grant type  # noqa: E501

        :param client_id: The client_id of this TokenRequest.
        :type client_id: str
        """
        if client_id is None:
            raise ValueError(
                "Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self) -> str:
        """Gets the client_secret of this TokenRequest.

        client app secret. Required for client_credentials grant_type  # noqa: E501

        :return: The client_secret of this TokenRequest.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret: str):
        """Sets the client_secret of this TokenRequest.

        client app secret. Required for client_credentials grant_type  # noqa: E501

        :param client_secret: The client_secret of this TokenRequest.
        :type client_secret: str
        """

        self._client_secret = client_secret

    @property
    def scope(self) -> str:
        """Gets the scope of this TokenRequest.

        The scopes which you want to request authorization for. These must be separated by a space  # noqa: E501

        :return: The scope of this TokenRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope: str):
        """Sets the scope of this TokenRequest.

        The scopes which you want to request authorization for. These must be separated by a space  # noqa: E501

        :param scope: The scope of this TokenRequest.
        :type scope: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def redirect_uri(self) -> str:
        """Gets the redirect_uri of this TokenRequest.

        This is required only if it was set at the GET /authorize endpoint. The values from /authorize must match the value you set at /oauth/token. Required for authorization_code and pkce grant_types  # noqa: E501

        :return: The redirect_uri of this TokenRequest.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri: str):
        """Sets the redirect_uri of this TokenRequest.

        This is required only if it was set at the GET /authorize endpoint. The values from /authorize must match the value you set at /oauth/token. Required for authorization_code and pkce grant_types  # noqa: E501

        :param redirect_uri: The redirect_uri of this TokenRequest.
        :type redirect_uri: str
        """

        self._redirect_uri = redirect_uri

    @property
    def code(self) -> str:
        """Gets the code of this TokenRequest.

        The Authorization Code received from the initial /authorize call. Required for PKCE  # noqa: E501

        :return: The code of this TokenRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this TokenRequest.

        The Authorization Code received from the initial /authorize call. Required for PKCE  # noqa: E501

        :param code: The code of this TokenRequest.
        :type code: str
        """

        self._code = code

    @property
    def code_verifier(self) -> str:
        """Gets the code_verifier of this TokenRequest.

        Cryptographically random key that was used to generate the code_challenge passed to /authorize. Required for PKCE  # noqa: E501

        :return: The code_verifier of this TokenRequest.
        :rtype: str
        """
        return self._code_verifier

    @code_verifier.setter
    def code_verifier(self, code_verifier: str):
        """Sets the code_verifier of this TokenRequest.

        Cryptographically random key that was used to generate the code_challenge passed to /authorize. Required for PKCE  # noqa: E501

        :param code_verifier: The code_verifier of this TokenRequest.
        :type code_verifier: str
        """

        self._code_verifier = code_verifier

    @property
    def refresh_token(self) -> str:
        """Gets the refresh_token of this TokenRequest.

        refresh token needed to regenerate JWT. Required for refresh grant_type  # noqa: E501

        :return: The refresh_token of this TokenRequest.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token: str):
        """Sets the refresh_token of this TokenRequest.

        refresh token needed to regenerate JWT. Required for refresh grant_type  # noqa: E501

        :param refresh_token: The refresh_token of this TokenRequest.
        :type refresh_token: str
        """

        self._refresh_token = refresh_token
