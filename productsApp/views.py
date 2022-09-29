from turtle import left, right
from django.shortcuts import render
from django.shortcuts import HttpResponse

from productsApp.models import Product
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.


# def robot(request):
#     html = '<html><body>家用机器人</body></html>'
#     return HttpResponse(html)


# def monitoring(request):
#     html = '<html><body>智能监控</body></html>'
#     return HttpResponse(html)


# def face(request):
#     html = '<html><body>人脸识别解决方案</body></html>'
#     return HttpResponse(html)

def products(request, productName):
    submenu = productName
    if productName == 'robot':
        productName = '家用机器人'
    elif productName == 'monitor':
        productName = '智能监控'
    else:
        productName = '人脸识别解决方案'
    
    # 待分页的数据
    productList = Product.objects.all().filter(
        productType=productName).order_by('-publishDate')

    # 获取分页器对象,把productList数据按照2个一页显示
    p = Paginator(productList, 2)
    # p.num_pages分页后的页面总数
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))  # 以page为键得到默认的页面1
        # 分类器方法page()接受一个必填参数即页码号，返回一个当前页对象，若不提供将返回一个 TypeError 错误
        productList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range   #分页后的页码范围page_range从1开始，不包括右,左闭右开
        if page == 1:
            right = page_range[page: page+2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page-3) if (page-3) > 0 else 0: page-1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2]         
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            # if right[-1] < total_pages - 1:
            #     right_has_more = True
            # if right[-1] < total_pages:
            #     last = True
        pageData = {                                 
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page,
        }

    return render(
        request, 'productList.html', {
            'active_menu': 'products',
            'sub_menu': submenu,
            'productName': productName,
            'productList': productList,
            'pageData': pageData,
        })

def productDetail(request, id):
    product = get_object_or_404(Product, id=id)
    product.views += 1
    product.save()
    return render(request, 'productDetail.html', {
        'active_menu': 'products',
        'product': product,
    })