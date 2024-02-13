from django.shortcuts import render
# from django.views import View
# from .models import Membership

# class CalculateNumbersView(View):
#     template_name = 'calculate_numbers.html'  # Set your desired template name

#     def get(self, request, *args, **kwargs):
#         memberships = Membership.objects.all()
#         total_sum = sum(membership.calculate_amount() for membership in memberships)
#         context = {'total_sum': total_sum}
#         return render(request, self.template_name, context)
