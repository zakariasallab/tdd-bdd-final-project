# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from faker import Faker
from service.models import Product, Category

# Initialize the Faker instance
fake = Faker()


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""
        model = Product

    id = factory.Sequence(lambda n: n)  # Auto-incrementing ID for each product
    name = factory.LazyAttribute(lambda _: fake.company())  # Random company name
    description = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=200))  # Random description text
    price = FuzzyDecimal(5.0, 1000.0, precision=2)  # Random price between 5 and 1000
    available = factory.LazyAttribute(lambda _: fake.boolean())  # Random True/False availability
    category = FuzzyChoice([Category.CLOTHS, Category.FOOD, Category.HOUSEWARES, Category.AUTOMOTIVE, Category.TOOLS])
