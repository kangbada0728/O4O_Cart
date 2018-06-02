def gnb_menus(request):
    menus = [
        {
            'name': '고객',
            'sub_menus': [
                {'name': '구매정보', 'url': '/admin/cart/pur_history/'},
                {'name': '이동정보', 'url': '/admin/cart/mv_history/'},
                {'name': '고객정보', 'url': '/admin/cart/customer_info/'},
                {'name': '카트', 'url': '/admin/cart/cart_info/'},
            ]
        },
        {
            'name': '상품',
            'sub_menus': [
                {'name': '종류', 'url': '/admin/cart/item_sort_info/'},
                {'name': '상품', 'url': '/admin/cart/items/'},
                {'name': '재고', 'url': '/admin/cart/item_info/'},
            ]
        },
        {
            'name': '서비스',
            'sub_menus': [
                {'name': '광고', 'url': '/admin/cart/ad_info/'},
                {'name': '상품쿠폰', 'url': '/admin/cart/coupons_item/'},
                {'name': '상품쿠폰재고', 'url': '/admin/cart/coupon_item_info/'},
                {'name': '카메라', 'url': '/admin/cart/camera_info/'},
            ]
        }
    ]
    return {'gnb_menus': menus}