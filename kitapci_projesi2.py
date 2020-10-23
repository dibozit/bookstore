from kitapci_projesi import BookStore
from kitapci_projesi import Book, Writer, Publisher, Genre, AppUser, Order, OrderDetails

db= BookStore()

while True:
    secim = input("""
    1. Kullanıcı girişi
    2. Yeni üye
    """)
    if secim == "1":
        isim = input("Lütfen kullanıcı isminizi giriniz")
        sonuc = db.FindUserRole(isim)
        if (sonuc == None):
            continue
        elif (sonuc=="Admin"):
            print("hoşgeldin Admin")
            while True:
                adminCrudSecim = input(""""
                Hangi alana gitmek istersiniz?
                1. Kitap
                2. Yazar
                3. Yayınevi
                4. Tür
                5. Kullanıcı
                6. Sipariş
                7. Log Out
                """)
                if adminCrudSecim=="1":
                    while True:
                        bookCrudSecim = input("""
                        1. Ekle
                        2. Sil
                        3. Güncelle
                        4. Görüntüle
                        5. Çık
                        """)
                        if bookCrudSecim == "1":
                            kitapIsmi = input("kitap ismi giriniz")
                            kitapFiyati = int(input("kitap fiyatını giriniz"))
                            db.ShowWriters()
                            yazarSoyismi = input("lütfen yazar soyismi giriniz")
                            yazarID = db.FindWriter(yazarSoyismi)
                            db.ShowGenres()
                            turIsmi = input("türü giriniz")
                            turID = db.FindGenre(turIsmi)
                            db.ShowPublishers()
                            yayineviIsmi = input("yayınevi giriniz")
                            yayineviID = db.FindPublisher(yayineviID)
                            book1 = Book(kitapIsmi,kitapFiyati,yazarID,yayineviID,turID)
                            db.AddBook(book1)
                        elif bookCrudSecim == "2":
                            db.ShowBooks()
                            silinecekKitap = input("silmek istediğiniz kitap adını giriniz")
                            db.DeleteBook(silinecekKitap)
                        elif bookCrudSecim == "3":
                            db.ShowBooks()
                            guncellenecekKitap = input("güncellemek istediğiniz kitabın adını giriniz")
                            db.FindBookID(guncellenecekKitap)
                            yeniIsim = input("kitabın güncel ismi nedir")
                            yeniFiyat = input("kitabın güncel fiyatını giriniz")
                            db.ShowWriters()
                            yazaribul = input("kitabın güncel yazarının soy ismini giriniz")
                            yeniYazar = db.FindWriter(yazaribul)
                            db.ShowPublishers()
                            yayinevibul = input("kitabın güncel yayınevinin ismini giriniz")
                            yeniYayinevi = db.FindPublisher(yayinevibul)
                            db.ShowGenres()
                            turubul = input("kitabın güncel türünü giriniz")
                            yeniTur = db.FindWriter(turubul)
                            db.UpdatedBook(guncellenecekKitap,yeniIsim,yeniFiyat,yeniYazar,yeniYayinevi,yeniTur)
                        elif bookCrudSecim == "4":
                            db.ShowBooks()
                        elif bookCrudSecim == "5":
                            print("çıkış yapılıyor")
                            break
                        else:
                            print("geçersiz giriş yaptınız, lütfen tekrar deneyiniz.")
                            continue

                elif adminCrudSecim == "2":
                    while True:
                        writerCrudSecim = input("""
                        1. Ekle
                        2. Sil
                        3. Güncelle
                        4. Görüntüle
                        5. Çık
                        """)
                        if writerCrudSecim == "1":
                            eklenecekIsim = input("eklemek istediğiniz yazarın adını giriniz")
                            eklenecekSoyisim = input("eklemek istediğiniz yazarın soyadını giriniz")
                            yazar = Writer(eklenecekIsim,eklenecekSoyisim)
                            db.AddWriter(yazar)
                        elif writerCrudSecim == "2":
                            db.ShowWriters()
                            silinecekSoyisim = input("silmek istediğiniz yazarın soyismini giriniz")
                            db.DeleteWriter(silinecekSoyisim)
                        elif writerCrudSecim == "3":
                            db.ShowWriters()
                            guncellenecekSoyisim = input("lütfen güncellemek istediğiniz yazarın soyismini giriniz")
                            yeniIsim = input("güncellemek istediğiniz yazarın adını giriniz")
                            yeniSoyisim = input("güncellemek istediğiniz yazarın soyadını giriniz")
                            db.UpdateWriter(guncellenecekSoyisim,yeniIsim, yeniSoyisim)
                        elif writerCrudSecim == "4":
                            db.ShowWriters()
                        elif writerCrudSecim == "5":
                            print("çıkış yapılıyor")
                            break
                        else:
                            print("geçersiz bir işlem yürüttünüz, tekrar deneyiniz")
                            continue

                elif adminCrudSecim == "3":
                    while True:
                        publisherCrudSecim = input("""
                        1. Ekle
                        2. Sil
                        3. Görüntüle
                        4. Çık
                        """)
                        if publisherCrudSecim == "1":
                            eklenecekYayınevi = input("eklemek istediğiniz yayınevinin adını giriniz")
                            a = Publisher(eklenecekYayınevi)
                            db.AddPublisher(a)
                        elif publisherCrudSecim == "2":
                            db.ShowPublishers()
                            silinecekYayinevi = input("silmek istediğiniz yayınevini giriniz")
                            db.DeletePublisher(silinecekYayinevi)
                        elif publisherCrudSecim == "3":
                            db.ShowPublishers()
                        elif publisherCrudSecim == "4":
                            print("çıkış yapılıyor")
                            break
                        else:
                            print("geçersiz bir işlem yürüttünüz, tekrar deneyiniz")
                            continue

                elif adminCrudSecim == "4":
                    while True:
                        genreCrudSecim = input("""
                        1. Ekle
                        2. Sil
                        3. Görüntüle
                        4. Çık
                        """)
                        if genreCrudSecim == "1":
                            eklenecekTur = input("eklemek istediğiniz türü giriniz")
                            a = Genre(eklenecekTur)
                            db.AddGenre(a)
                        elif genreCrudSecim == "2":
                            db.ShowGenres()
                            silinecekTur = input("silmek istediğiniz türü giriniz")
                            db.DeleteGenre(silinecekTur)
                        elif genreCrudSecim == "3":
                            db.ShowGenres()
                        elif genreCrudSecim == "4":
                            print("çıkış yapılıyor")
                            break
                        else:
                            print("geçersiz bir işlem yürüttünüz, tekrar deneyiniz")
                            continue

                elif adminCrudSecim == "5":
                    while True:
                        userCrudSecim = input("""
                        1. Ekle
                        2. Sil
                        3. Güncelle
                        4. Görüntüle
                        5. Çık
                        """)
                        if userCrudSecim == "1":
                            userName = input("kullanıcı adı giriniz")
                            password = input("şifre giriniz")
                            user = AppUser(userName,password)
                            db.AddUser(user)
                        elif userCrudSecim == "2":
                            db.ShowUser()
                            silinecekKullanici = input("silmek istediğiniz kullanıcının adını giriniz")
                            db.DeleteAppUser(silinecekKullanici)
                        elif userCrudSecim == "3":
                            guncellenecekKullanici = input("güncellemek istediğiniz kullanıcının adını giriniz")
                            yeniSifre = input("güncel kullanıcı sifresini giriniz")
                            _yeniRol = input("kullanıcının rolünü Admin veya Member olarak belirleyiniz")
                            while _yeniRol == "Admin" or _yeniRol== "Member":
                                yeniRol = _yeniRol
                            else:
                                print("yeniden giriş yapınız")
                                continue
                            #bunu kontrol et çalıştı mı diye
                            db.UpdateAppUser(guncellenecekKullanici,yeniSifre,yeniRol)
                        elif userCrudSecim == "4":
                            db.ShowUser()
                        elif userCrudSecim == "5":
                            print("çıkış yapılıyor")
                            break
                        else:
                            print("geçersiz bir işlem yürüttünüz, tekrar deneyiniz")
                            continue

                elif adminCrudSecim == "6":
                    while True:
                        orderCrudSecim = input("""
                        1. Ekle
                        2. Sil
                        3. Çık
                        """)
                        if orderCrudSecim == "1":
                            eklenecekSiparis = input("eklemek istediğiniz sipariş için adres giriniz")
                            a = Order(eklenecekSiparis)
                            db.AddOrder(a)
                            sonSiparis = db.FindOrderID()
                            db.ShowBooks()
                            Kitap = input("lütfen istediğiniz kitabın adını giriniz")
                            istenenKitap = db.FindBookID(Kitap)
                            siparis = OrderDetails(sonSiparis,istenenKitap)
                            db.AddOrderDetails(siparis)
                            print(" {} numaralı siparişiniz işleme girmiştir").format(sonSiparis)
                        elif orderCrudSecim == "2":
                            silinecekSiparisNo = input("silmek istediğiniz siparişin numarasını giriniz")
                            db.DeleteOrder(silinecekSiparisNo)
                        elif orderCrudSecim == "3":
                            print("çıkış yapılıyor")
                            break
                        else:
                            print("geçersiz bir işlem yürüttünüz, tekrar deneyiniz")
                            continue
                elif adminCrudSecim == "7":
                    print("çıkış yapılıyor")
                    db.EndConnection()
                    break
                else:
                    print("geçersiz bir işlem yürüttünüz")
                    continue
    elif secim == "2":
        isim = input("lütfen yaratmak istediğiniz kullanıcı için isim giriniz")
        sifre = input("lütfen yaratmak istediğiniz kullanıcı için şifre giriniz")
        kullanici = AppUser(isim,sifre)
        db.AddUser(kullanici)

    else:
        print("geçersiz işlem yürüttünüz, lütfen tekrar deneyiniz")
        continue

