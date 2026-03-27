from django.db import transaction
from apps.organizations.models import Organization
from apps.memberships.models import Membership, Role

class OrganizationService:
    @classmethod
    @transaction.atomic
    def create_organization(cls, *, name, owner):
        if not name:
            raise ValueError("Organization name is required")

        org = Organization.objects.create(
            name=name,
            owner=owner,
        )

        Membership.objects.create(
            user=owner,
            organization=org,
            role=Role.OWNER,
        )

        return org
