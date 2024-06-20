# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ChangePasswordBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, password: str=None):  # noqa: E501
        """ChangePasswordBody - a model defined in Swagger

        :param password: The password of this ChangePasswordBody.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {'password': str}

        self.attribute_map = {'password': 'password'}
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'ChangePasswordBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChangePasswordBody of this ChangePasswordBody.  # noqa: E501
        :rtype: ChangePasswordBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def password(self) -> str:
        """Gets the password of this ChangePasswordBody.


        :return: The password of this ChangePasswordBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this ChangePasswordBody.


        :param password: The password of this ChangePasswordBody.
        :type password: str
        """

        self._password = password
