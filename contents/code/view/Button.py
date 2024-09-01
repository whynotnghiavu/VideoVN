from view.UseCase import UseCase
from view.THEMES import THEMES


class Button():
    button_themes = {
        UseCase.KiemTraAmThanh: THEMES.DOC_LAP,
        UseCase.XoaManHinh: THEMES.DOC_LAP,
        UseCase.ChonThuMuc: THEMES.CHON_THU_MUC,
        UseCase.GhiThongTin: THEMES.DOC_LAP,

        UseCase.TatCa1: THEMES.TAT_CA,
        UseCase.LuuCauTrucThuMuc: THEMES.BINH_THUONG,
        UseCase.SaoChepThuMuc: THEMES.BINH_THUONG,
        UseCase.XoaFileKhongDung: THEMES.DOC_LAP,
        UseCase.DoiTenFolderCon: THEMES.BINH_THUONG,
        UseCase.DoiTenFileCon: THEMES.BINH_THUONG,
        UseCase.KiemTraTenGiongNhau: THEMES.BINH_THUONG,
        UseCase.TaoFileSubRieng: THEMES.BINH_THUONG,
        UseCase.HopNhatCauSub: THEMES.BINH_THUONG,
        UseCase.HopNhatTatCaFileSub: THEMES.BINH_THUONG,

        UseCase.DichTiengViet: THEMES.DAC_BIET,

        UseCase.TatCa2: THEMES.TAT_CA,
        UseCase.XuLyFileKetQuaDich: THEMES.DOC_LAP,
        UseCase.TachFileSub: THEMES.BINH_THUONG,
        UseCase.TatCa3: THEMES.TAT_CA,
        UseCase.ChuyenAmThanh: THEMES.BINH_THUONG,
        UseCase.ThemAmThanh: THEMES.BINH_THUONG,
        UseCase.HopAmThanh: THEMES.BINH_THUONG,
        UseCase.GhepAmThanh: THEMES.BINH_THUONG,
        UseCase.DonDep: THEMES.BINH_THUONG,
        UseCase.DoiTenFileSub: THEMES.BINH_THUONG,

        UseCase.XoaFileSub: THEMES.DOC_LAP,
        UseCase.ThoatChuongTrinh: THEMES.EXIT,
    }
