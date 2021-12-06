from sqlalchemy import exc
from __init__ import db,app
from models import *
import os
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
class KhachHangController():
    def saveImg(self,img,filename):
        if not (img and self.allowed_file(img.filename)):
            return None
        path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(path) 
        return filename
    def insert(self,data):
        HoTenKH=data['HoTenKH']
        GioiTinh=data['GioiTinh']
        NamSinh=data['NamSinh']
        SDT=data['SDT']
        CMND=data['CMND']
        Email=data['Email']
        HinhAnh = data['HinhAnh']
        id_nguoidung=data['id_nguoidung']

        kh = KhachHang(HoTenKH=HoTenKH,GioiTinh=GioiTinh,
                       NamSinh=NamSinh,SDT=SDT,
                       CMND=CMND,Email=Email,id_nguoidung=id_nguoidung)
        db.session.add(kh)
        db.session.flush()
        db.session.refresh(kh)
        id= kh.id
        filename= 'hinhAnh'+str(id)+'.png'
        HinhAnh=self.saveImg(HinhAnh,filename)
        kh.HinhAnh=HinhAnh
        return kh
        
    
    def delete(self,kh):
        db.session.delete(kh)
        
    def search(self,search):
        search= "%"+search.strip()+"%"
        return KhachHang.query.filter(KhachHang.HoTenKH.like(search)).all()
    
    def getAll(self):
        return KhachHang.query.all()
    
    def maxPage(self,list):
        lenList = len(list)
        maxInPage=5
        du = 1 if lenList%maxInPage!=0 else 0
        return int(lenList/maxInPage)+du
    
    def listInPage(self,page,list):
        lenList = len(list)
        maxInPage=5
        start = (page-1) * maxInPage
        end = start+maxInPage
        if(end>lenList):
            return list[start:]
        else:
            return list[start:end]

    def allowed_file(self,filename):
	    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

