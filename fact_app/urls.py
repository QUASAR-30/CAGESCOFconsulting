from django.urls import path
from . import views
from .views import IndexClientView
urlpatterns = [ 
   
    path('', views.HomeView.as_view(), name='home'),
    path('prince/', views.HomeViewDoc.as_view(), name='home'),

    path('indexclient/', IndexClientView.as_view(), name='indexclient'),

    path('add-customer', views.AddCustomerView.as_view(), name='add-customer'),
    path('add-document', views.AddDocumentView.as_view(), name='add-document'),
    path('add-invoice', views.AddInvoiceView.as_view(), name='add-invoice'),
    path('view-invoice/<int:pk>', views.InvoiceVisualizationView.as_view(), name='view-invoice'),
    path('invoice-pdf/<int:pk>', views.get_invoice_pdf, name="invoice-pdf")
]