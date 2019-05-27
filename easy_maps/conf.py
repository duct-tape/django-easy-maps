# -*- coding: utf-8 -*-

import warnings

from django.conf import settings  # pylint: disable=W0611

from appconf import AppConf


class EasyMapsSettings(AppConf):
    CENTER = (-41.3, 32)
    GEOCODE = 'easy_maps.geocode.google_v3'
    ZOOM = 16  # See https://developers.google.com/maps/documentation/javascript/tutorial#MapOptions for more information.
    LANGUAGE = 'en'  # See https://developers.google.com/maps/faq#languagesupport for supported languages.
    GOOGLE_MAPS_API_KEY = None
    GOOGLE_KEY = None

    CACHE_LIFETIME = 600  # 10 minutes in seconds

    class Meta:
        prefix = 'easy_maps'
        holder = 'easy_maps.conf.settings'

if settings.EASY_MAPS_GOOGLE_MAPS_API_KEY is not None:
    warnings.warn("EASY_MAPS_GOOGLE_MAPS_API_KEY is deprecated, use EASY_MAPS_GOOGLE_KEY", DeprecationWarning)
