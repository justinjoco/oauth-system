# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RolePermission(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self,
                 id: str=None,
                 role_name: str=None,
                 permission_value: str=None):  # noqa: E501
        """RolePermission - a model defined in Swagger

        :param id: The id of this RolePermission.  # noqa: E501
        :type id: str
        :param role_name: The role_name of this RolePermission.  # noqa: E501
        :type role_name: str
        :param permission_value: The permission_value of this RolePermission.  # noqa: E501
        :type permission_value: str
        """
        self.swagger_types = {
            'id': str,
            'role_name': str,
            'permission_value': str
        }

        self.attribute_map = {
            'id': 'id',
            'role_name': 'roleName',
            'permission_value': 'permissionValue'
        }
        self._id = id
        self._role_name = role_name
        self._permission_value = permission_value

    @classmethod
    def from_dict(cls, dikt) -> 'RolePermission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RolePermission of this RolePermission.  # noqa: E501
        :rtype: RolePermission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this RolePermission.


        :return: The id of this RolePermission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this RolePermission.


        :param id: The id of this RolePermission.
        :type id: str
        """

        self._id = id

    @property
    def role_name(self) -> str:
        """Gets the role_name of this RolePermission.


        :return: The role_name of this RolePermission.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name: str):
        """Sets the role_name of this RolePermission.


        :param role_name: The role_name of this RolePermission.
        :type role_name: str
        """

        self._role_name = role_name

    @property
    def permission_value(self) -> str:
        """Gets the permission_value of this RolePermission.


        :return: The permission_value of this RolePermission.
        :rtype: str
        """
        return self._permission_value

    @permission_value.setter
    def permission_value(self, permission_value: str):
        """Sets the permission_value of this RolePermission.


        :param permission_value: The permission_value of this RolePermission.
        :type permission_value: str
        """

        self._permission_value = permission_value
