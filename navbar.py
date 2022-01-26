import hydralit_components as hc

def navbar():
    menu_data = [
        {'id':'Scrape Data From Twitter', 'icon': 'fab fa-twitter', 'label':'Scrape Data From Twitter'},
        {'id':'Text Preprocessing', 'icon': 'fas fa-cogs', 'label':'Text Preprocessing'},
        {'id':'Topic Detection', 'icon': 'fas fa-search', 'label':'Topic Detection'},
        # {'id':'Topic Tracking', 'icon': 'fas fa-angle-double-right', 'label':'Topic Tracking'},
    ] 

    over_them = {'txc_inacive': '#FFFFFF'}
    menu_id = hc.nav_bar(menu_definition=menu_data, 
                        override_theme=over_them,
                        home_name='Home', 
                        first_select=0,
                        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
                        sticky_nav=True, #at the top or not
                        sticky_mode='pinned') #jumpy or not-jumpy, but sticky or pinned
        
                        
                        
    return menu_id
