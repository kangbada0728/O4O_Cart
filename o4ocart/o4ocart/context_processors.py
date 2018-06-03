def gnb_menus(request):
    menus = [
        {
            'name': '고객',
            'sub_menus': [
                {'name': '구매정보', 'url': '/admin/cart/pur_history/'},
                {'name': '고객정보', 'url': '/admin/cart/customer_info/'},
                {'name': '카트정보', 'url': '/admin/cart/cart_info/'},
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
            ]
        },
        {
            'name': '시각화',
            'sub_menus': [
                {'name': '고객 이동경로', 'url': '/admin/draw/img_selector/'},
            ]
        },
        {
            'name': '기타',
            'sub_menus': [
                {'name': '이동정보관리', 'url': '/admin/cart/mv_history/'},
                {'name': '카메라 관리', 'url': '/admin/cart/camera_info/'},
                {'name': '영역 설정', 'url': '/admin/cart/matrix/'},
            ]
        }
    ]
    return {'gnb_menus': menus}
