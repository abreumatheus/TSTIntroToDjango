from typing import List

from seller.models import Seller


class SellerController:
    def get_all(self) -> List[Seller]:
        return Seller.objects.all()

    def get_by_id(self, id: int) -> Seller:
        return Seller.objects.filter(id=id).get()

    def create(self, full_name: str, email: str) -> Seller:
        seller = Seller(full_name=full_name, email=email)
        seller.save()
        return seller

    def update(self, id: int, full_name: str, email: str) -> Seller:
        seller = self.get_by_id(id)
        seller.full_name = full_name
        seller.email = email
        seller.save()
        return seller

    def delete(self, id: int) -> None:
        seller = self.get_by_id(id)
        seller.delete()
