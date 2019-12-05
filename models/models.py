# -*- coding: utf-8 -*-

from odoo import models, fields, api


class po_tracking(models.Model):
    _name = "purchase.order.line"
    _inherit = "purchase.order.line"

    
    tgl_buat_pr = fields.Data(string="Tanggal Buat PR")
    nomor_pr  = fields.Integer(string="Nomer PR")
    deskripsi = fields.Text(string="Deskripsi")
    wilayah = fields.Char(string="Wilayah")
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