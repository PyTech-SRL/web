from odoo import models

class ResCompany(models.Model):
    _inherit = "res.company"

    def _get_scss_template(self):
        return (
            super()._get_scss_template()
            + """
             .o_menu_apps .dropdown-menu {
                background: url('/web_responsive/static/img/home-menu-bg-overlay.svg'),
                  linear-gradient(
                    to bottom,
                    %(color_navbar_bg)s,
                    desaturate(lighten(%(color_navbar_bg)s, 20%%), 15)
                  );
             }
             .o_purchase_dashboard .table > thead > tr > td.o_main, 
             .o_purchase_dashboard .table > tbody > tr > td.o_main {
                background-color: %(color_navbar_bg)s !important;
             }
             .o_searchview .o_searchview_autocomplete li.o_selection_focus {
                background-color: %(color_navbar_bg)s !important;
             }
             .o_searchview .o_searchview_facet {
                background: %(color_navbar_bg)s-lightsecondary;
             }
            """
        )
      
    def _get_scss_template_uninstall(self):
        return super()._get_scss_template()