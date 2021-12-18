import hydralit_components as hc
def navbar():
    menu_data = [
        {'id':'Scrape Data From Twitter', 'icon': 'fab fa-twitter', 'label':'Scrape Data From Twitter'},
        {'id':'Topic Detection', 'icon': 'fas fa-search', 'label':'Topic Detection'},
        {'id':'Topic Tracking', 'icon': 'fas fa-angle-double-right', 'label':'Topic Tracking'},
    ] 

    over_them = {'txc_inacive': '#FFFFF'}
    menu_id = hc.nav_bar(menu_definition=menu_data, override_theme=over_them,home_name='Home', first_select=0)
    return menu_id
