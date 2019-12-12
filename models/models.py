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
    nilai_pr = fields.Float(string="Nilai PR",)
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
            line_pr = []
            for line_pa in pa.line_ids:
                for line_dep in line_pa.line_department_ids:
                    tgl_buat_pr.append(line_dep.request_id.date.strftime("%d-%b-%Y"))
                    nomor_pr.append(line_dep.request_id.name)
                    deskripsi.append(line_dep.request_id.notes)
                    wilayah.append(line_dep.request_id.location_id.name)
            rec.tgl_buat_pr = ",".join(tgl_buat_pr)
            rec.nomor_pr = nomor_pr
            rec.deskripsi = deskripsi
            rec.wilayah = wilayah
            
    def get_line_pr(self):
        pa_obj = self.env["purchase.requisition"]
        pr_obj = self.env["product.product"]
        for rec in self:  # rec = po line
            pa = pa_obj.search([("name", "=", rec.order_id.origin)])
            line_pr = []
            for line_pa in pa.line_ids:
                for line_dep in line_pa.line_department_ids:
                    tgl_buat_pr.append(line_dep.request_id.date.strftime("%d-%b-%Y"))
            rec.tgl_buat_pr = ",".join(tgl_buat_pr)
            rec.nomor_pr = nomor_pr
