from tkinter import messagebox


from view.UseCase import UseCase


from modules.MyLog import MyLog


from modules.ShutdownComputer import ShutdownComputer


from modules.KiemTraAmThanh import KiemTraAmThanh


from modules.XoaManHinh import XoaManHinh


from modules.ChonThuMuc import ChonThuMuc


from modules.GhiThongTin import GhiThongTin


from modules.LuuCauTrucThuMuc import LuuCauTrucThuMuc


from modules.SaoChepThuMuc import SaoChepThuMuc


from modules.XoaFileKhongDung import XoaFileKhongDung


from modules.DoiTenFolderCon import DoiTenFolderCon


from modules.DoiTenFileCon import DoiTenFileCon


from modules.KiemTraTenGiongNhau import KiemTraTenGiongNhau


from modules.TaoFileSubRieng import TaoFileSubRieng


from modules.HopNhatCauSub import HopNhatCauSub


from modules.HopNhatTatCaFileSub import HopNhatTatCaFileSub


from modules.DichTiengViet import DichTiengViet


from modules.XuLyFileKetQuaDich import XuLyFileKetQuaDich


from modules.TachFileSub import TachFileSub


from modules.ChuyenAmThanh import ChuyenAmThanh


from modules.ThemAmThanh import ThemAmThanh


from modules.HopAmThanh import HopAmThanh


from modules.GhepAmThanh import GhepAmThanh


from modules.DonDep import DonDep


from modules.DoiTenFileSub import DoiTenFileSub


from modules.XoaFileSub import XoaFileSub


def ButtonClick(chuc_nang, var_shutdown):
    MyLog.title(f"Bắt đầu chức năng: {chuc_nang}")
    Router(chuc_nang)
    MyLog.title(f"Kết thúc chức năng: {chuc_nang}")

    excluded_cases = [
        UseCase.KiemTraAmThanh,
        UseCase.XoaManHinh,
        UseCase.GhiThongTin,
    ]
    if chuc_nang not in excluded_cases:
        GhiThongTin(root_dir)

    if chuc_nang == UseCase.TatCa2:
        if var_shutdown.get():
            MyLog.error("Tự động tắt máy")
            ShutdownComputer()


def Router(chuc_nang):
    global root_dir
    if chuc_nang == "":
        MyLog.error(chuc_nang)
        MyLog.error(UseCase.error)
        messagebox.showerror("Thông báo", UseCase.error)

    # NOTE: Chỉnh chức năng trong vùng này

    elif chuc_nang == UseCase.KiemTraAmThanh:
        KiemTraAmThanh()

    elif chuc_nang == UseCase.XoaManHinh:
        XoaManHinh()

    elif chuc_nang == UseCase.ChonThuMuc:
        root_dir = ChonThuMuc()

    elif chuc_nang == UseCase.GhiThongTin:
        GhiThongTin(root_dir)

    elif chuc_nang == UseCase.TatCa1:
        LuuCauTrucThuMuc(root_dir)
        root_dir = SaoChepThuMuc(root_dir)
        XoaFileKhongDung(root_dir)
        DoiTenFolderCon(root_dir)
        DoiTenFileCon(root_dir)
        KiemTraTenGiongNhau(root_dir)
        TaoFileSubRieng(root_dir)
        HopNhatCauSub(root_dir)
        HopNhatTatCaFileSub(root_dir)

    elif chuc_nang == UseCase.LuuCauTrucThuMuc:
        LuuCauTrucThuMuc(root_dir)

    elif chuc_nang == UseCase.SaoChepThuMuc:
        root_dir = SaoChepThuMuc(root_dir)

    elif chuc_nang == UseCase.XoaFileKhongDung:
        XoaFileKhongDung(root_dir)

    elif chuc_nang == UseCase.DoiTenFolderCon:
        DoiTenFolderCon(root_dir)

    elif chuc_nang == UseCase.DoiTenFileCon:
        DoiTenFileCon(root_dir)

    elif chuc_nang == UseCase.KiemTraTenGiongNhau:
        KiemTraTenGiongNhau(root_dir)

    elif chuc_nang == UseCase.TaoFileSubRieng:
        TaoFileSubRieng(root_dir)

    elif chuc_nang == UseCase.HopNhatCauSub:
        HopNhatCauSub(root_dir)

    elif chuc_nang == UseCase.HopNhatTatCaFileSub:
        HopNhatTatCaFileSub(root_dir)

    elif chuc_nang == UseCase.DichTiengViet:
        DichTiengViet()

    elif chuc_nang == UseCase.XuLyFileKetQuaDich:
        XuLyFileKetQuaDich()

    elif chuc_nang == UseCase.TatCa2:
        XuLyFileKetQuaDich()
        TachFileSub(root_dir)

        ChuyenAmThanh(root_dir)
        ThemAmThanh(root_dir)
        HopAmThanh(root_dir)
        GhepAmThanh(root_dir)

        DonDep(root_dir)
        DoiTenFileSub(root_dir)

    elif chuc_nang == UseCase.TachFileSub:
        TachFileSub(root_dir)

    elif chuc_nang == UseCase.ChuyenAmThanh:
        ChuyenAmThanh(root_dir)

    elif chuc_nang == UseCase.ThemAmThanh:
        ThemAmThanh(root_dir)

    elif chuc_nang == UseCase.HopAmThanh:
        HopAmThanh(root_dir)

    elif chuc_nang == UseCase.GhepAmThanh:
        GhepAmThanh(root_dir)

    elif chuc_nang == UseCase.DonDep:
        DonDep(root_dir)

    elif chuc_nang == UseCase.DoiTenFileSub:
        DoiTenFileSub(root_dir)

    elif chuc_nang == UseCase.XoaFileSub:
        XoaFileSub(root_dir)

    # ! Chỉ chỉnh các chức năng trong vùng này

    elif chuc_nang == UseCase.ThoatChuongTrinh:
        exit()
    else:
        MyLog.error(chuc_nang)
        MyLog.error(UseCase.error)
        messagebox.showerror("Thông báo", UseCase.error)
