#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ItemPipeline(object):
    def process_item(self, item):
        pass
