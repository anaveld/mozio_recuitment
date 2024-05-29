from django.test import TestCase
from django.contrib.gis.geos import LinearRing, Point, Polygon
from django.urls import reverse

from rest_framework.test import APITestCase

from app import constants
from core.models import Provider, ServiceArea
from core.search import search_areas


class SearchTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.provider1 = Provider.objects.create(
            name='Provider1',
            email='company@provider1.com',
            language=constants.ENG,
            currency=constants.USD,
        )
        cls.provider2 = Provider.objects.create(
            name='Provider2',
            email='company@provider2.com',
            language=constants.ENG,
            currency=constants.MXN,
        )
        cls.service_area1 = ServiceArea.objects.create(
            provider=cls.provider1,
            name='Area1',
            price=45.4,
            area=Polygon(
                LinearRing(
                    (52.234649, 20.990863),
                    (52.244072, 21.012533),
                    (52.221034, 21.010665),
                    (52.234649, 20.990863),
                ),
            ),  # area around Palace of Culture and Science in Warsaw
        )
        cls.service_area2 = ServiceArea.objects.create(
            provider=cls.provider1,
            name='Area2',
            price=12.5,
            area=Polygon(
                LinearRing(
                    (52.181694, 20.986244),
                    (52.186453, 20.947198),
                    (52.150139, 20.933370),
                    (52.141122, 21.013808),
                    (52.181694, 20.986244),
                ),
            )  # area around Chopin Airport in Warsaw
        )
        cls.service_area3 = ServiceArea.objects.create(
            provider=cls.provider2,
            name='Area3',
            price=3.45,
            area=Polygon(
                LinearRing(
                    (53.845926, 15.007950),
                    (53.855171, 23.416865),
                    (49.342948, 22.944714),
                    (51.009514, 15.015807),
                    (53.845926, 15.007950),
                ),
            )  # area around Poland
        )
        cls.service_area4 = ServiceArea.objects.create(
            provider=cls.provider2,
            name='Area4',
            price=102.5543,
            area=Polygon(
                LinearRing(
                    (53.802642, 9.541698),
                    (53.707234, 10.962945),
                    (53.022989, 9.822359),
                    (53.802642, 9.541698),
                ),
            )  # city of Hamburg in Germany
        )

    def test_search__returns_single_provider(self):
        search_results = search_areas(53.557647, 9.984059)  # point in Hamburg
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0].provider.name, self.provider2.name)
        self.assertEqual(search_results[0].full_price, '102.55 MEXICAN_PESO')

    def test_search__returns_no_provider(self):
        search_results = search_areas(19.419435, -99.140243)  # city of Mexico
        self.assertEqual(len(search_results), 0)

    def test_search__returns_multiple_providers(self):
        search_results = search_areas(52.231601, 21.006043)  # Palace of Culture and Science
        self.assertEqual(len(search_results), 2)
        self.assertEqual(search_results[0].provider.name, self.provider2.name)
        self.assertEqual(search_results[0].full_price, '3.45 MEXICAN_PESO')

        self.assertEqual(search_results[1].provider.name, self.provider1.name)
        self.assertEqual(search_results[1].full_price, '45.40 US_DOLLAR')
