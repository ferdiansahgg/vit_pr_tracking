# -*- coding: utf-8 -*-

from odoo import models, fields, api


class po_tracking(models.Model):
    _name = "purchase.order.line"
    _inherit = "purchase.order.line"

    tgl_buat_pr = fields.Char(string="Tanggal Buat PR", compute="get_pr")
    nomor_pr = fields.Char(string="Nomer PR", compute="get_pr")
    deskripsi = fields.Char(string="Deskripsi", compute="get_pr")
    wilayah = fields.Char(string="Wilayah", compute="get_pr")
    line_pr = fields.Char(string="Line PR", compute="get_line_pr")
    nilai_pr = fields.Float(string="Nilai PR", compute="get_line_pr")
    diperiksa = fields.Char(string="Diperiksa")
    konfirmasi_budget = fields.Char(string="Konfirmasi Budget",)
    disetujui = fields.Char(string="Disetujui",)
    tgl_diterima = fields.Datetime(string="Tanggal Diterima",)
    proses_pengadaan = fields.Char(string="Proses Pengadaan",)
    reject_pr = fields.Char(string="Reject PR",)
    nomor_po = fields.Char(string="Nomor PO",)

    bakn = fields.Char(string="BAKN")
    tgl_share_po = fields.Date(string="Tanggal Share PO")
    efisiensi_rp = fields.Char(string="Efisiensi RP")
    efisiensi_percent = fields.Char(string="Efesiensi Percent")
    kpi = fields.Char(string="KPI")
    sla = fields.Char(string="SLA")

    def get_pr(self):
        pa_obj = self.env["purchase.requisition"]
        pr_obj = self.env["vit.product.request"]
        for rec in self:  # rec = po line
            pa = pa_obj.search([("name", "=", rec.order_id.origin)])
            tgl_buat_pr = []
            nomor_pr = []
            deskripsi = []
            wilayah = []
            for line_pa in pa.line_ids:
                for line_dep in line_pa.line_department_ids:
                    tgl_buat_pr.append(line_dep.request_id.date.strftime("%d-%b-%Y"))
                    nomor_pr.append(line_dep.request_id.name)
                    deskripsi.append(
                        line_dep.request_id.notes if line_dep.request_id.notes else ""
                    )
                    wilayah.append(
                        line_dep.request_id.location_id.name
                        if line_dep.request_id.location_id
                        else ""
                    )
            rec.tgl_buat_pr = ",".join(tgl_buat_pr)
            rec.nomor_pr = ",".join(nomor_pr)
            rec.deskripsi = ",".join(deskripsi)
            rec.wilayah = ",".join(wilayah)

    def get_line_pr(self):
        pa_obj = self.env["purchase.requisition"]
        pr_obj = self.env["vit.product.request"]
        for rec in self:  # rec = po line
            pa = pa_obj.search([("name", "=", rec.order_id.origin)])
            line_pr = []
            nilai_pr = []
            for line_pa in pa.line_ids:
                for line_dep in line_pa.line_department_ids:
                    line_pr.append(
                        line_dep.pr_line_id.product_id.name
                        if line_dep.pr_line_id.product_id
                        else ""
                    )
                    # nilai_pr.append(
                    #     line_dep.request_id.product_request_line_ids.unit_price
                    #     if line_dep.request_id.product_request_line_ids.unit_price
                    #     else ""
                    # )

            rec.line_pr = ",".join(line_pr)
            # rec.nilai_pr = ",".join(nilai_pr)
