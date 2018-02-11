from datetime import datetime
from nurserylabels.models import PreviousLabelOrder


class NurseryLabelDAL:

    def get_previous_label_orders(self, user):
        return PreviousLabelOrder.objects.filter(user=user).order_by('datetime')

    def create_previous_label_order(self, user, data):
        order = PreviousLabelOrder()
        order.user = user
        order.data = data
        order.datetime = datetime.now()
        order.save()
        return order

    def delete_previous_labor_order(self, obj_id):
        obj = PreviousLabelOrder.objects.get(pk=obj_id)
        obj.delete()

NURSERY_LABEL_DAL = NurseryLabelDAL()
