#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
import json

from django.test import TestCase


class AppTestCase(TestCase):

    def test_frontpage(self):
        """Check if the front is correct"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

