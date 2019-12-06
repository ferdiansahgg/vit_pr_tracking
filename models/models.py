# -*- coding: utf-8 -*-

from odoo import models, fields, api


class po_tracking(models.Model):
    _name = "purchase.order.line"
    _inherit = "purchase.order.line"

    tgl_buat_pr = fields.Date(
        comodel_name="vit.po_line_department",
        string="Tanggal Buat PR",
        related="line_department_ids.request_id.date",
        # store=True,
    )
    nomor_pr = fields.Char(
        comodel_name="vit.po_line_department",
        string="Nomer PR",
        related="line_department_ids.request_id.name",
        # store=True,
    )
    deskripsi = fields.Text(
        comodel_name="vit.po_line_department",
        string="Deskripsi",
        related="line_department_ids.request_id.notes",
        store=True,
    )
    wilayah = fields.Char(
        comodel_name="vit.po_line_department",
        string="Wilayah",
        related="line_department_ids.request_id.location_id.name",
        # store=True,
    )
    line_pr = fields.Char(string="Line PR")
    nilai_pr = fields.Integer(string="Nilai PR")
    diperiksa = fields.Char(string="Diperiksa")
    konfirmasi_budget = fields.Char(string="Konfirmasi Budget")
    disetujui = fields.Char(string="Disetujui")
    tgl_diterima = fields.Date(string="Tanggal Diterima")
    proses_pengadaan = fields.Char(string="Proses Pengadaan")
    reject_pr = fields.Char(string="Reject PR")
    nomor_po = fields.Integer(string="Nomor PO")
    tgl_po = fields.Date(string="Tanggal PO")
    line_po = fields.Char(string="Line PO")
    nilai_po = fields.Integer(string="Nilai PO")
    vendor = fields.Char(string="Vendor")
    bakn = fields.Char(string="BAKN")
    tgl_share_po = fields.Date(string="Tanggal Share PO")
    efisiensi_rp = fields.Char(string="Efisiensi RP")
    efisiensi_percent = fields.Char(string="Efesiensi Percent")
    kpi = fields.Char(string="KPI")
    sla = fields.Char(string="SLA")

    # def get_date(self):
    #     l = self.line_ids
    #     d = l.line_deparment_ids
    #     r = d.request_id
    #     for x in r:
    #         self.tgl_buat_pr = x.date
