import sqlite3
from abc import ABC, abstractmethod
import datetime


class BaseEntity(ABC):
    def __init__(self):
        self.CreatedDate = datetime.datetime.now()
        self.DeletedDate = None
        self.UpdatedDate = None
        self.CreatedBy = None
        self.ModifiedBy = None
        self.DeletedBy = None


class Book(BaseEntity):
    # select b.BookName,w.WriterName from books as b join writers as w
    def __init__(self, _bookName, _price, _writerID=None, _publisherID=None, _genreID=None, _bookID=None):
        BaseEntity.__init__(self)
        self.BookName = _bookName
        self.Price = _price
        self.WriterID = _writerID
        self.PublisherID = _publisherID
        self.GenreID = _genreID
        self.BookID = _bookID

    def __str__(self):
        return self.BookName


class Writer(BaseEntity):
    def __init__(self, _writerName, _writerSurname, _writerID=None):
        BaseEntity.__init__(self)
        self.WriterName = _writerName
        self.WriterSurname = _writerSurname
        self.WriterID = _writerID

    def __str__(self):
        return "{} {}".format(self.WriterName, self.WriterSurname)


class Publisher(BaseEntity):
    def __init__(self, _publisherName, _publisherID=None):
        BaseEntity.__init__(self)
        self.PublisherName = _publisherName
        self.PublisherID = _publisherID

    def __str__(self):
        return self.PublisherName


class Genre(BaseEntity):
    def __init__(self, _genreName, _genreID=None):
        BaseEntity.__init__(self)
        self.GenreName = _genreName
        self.GenreID = _genreID

    def __str__(self):
        return self.GenreName


class AppUser(BaseEntity):
    def __init__(self, _appUserName, _password, _role="Member", _appUserID=None):
        BaseEntity.__init__(self)
        self.AppUserName = _appUserName
        self.Password = _password
        if _appUserName == "Admin" and _password == "123":
            self.Role = "Admin"
        else:
            self.Role = _role
        self.AppUserID = _appUserID


class Order(BaseEntity):
    def __init__(self, _shippedAddress, _orderID=None):
        BaseEntity.__init__(self)
        self.ShippedAddress = _shippedAddress
        self.OrderID = _orderID


class OrderDetails(BaseEntity):
    def __init__(self, _orderID, _bookID):
        BaseEntity.__init__(self)
        self.OrderID = _orderID
        self.BookID = _bookID


class BookStore:
    def __CreateConnection(self):
        self.__Connection = sqlite3.connect("BookStore.DB")
        self.__cursor = self.__Connection.cursor()
        writers = "create table if not exists Writer(WriterID integer primary key autoincrement, WriterName text, WriterSurname text)"
        publishers = "create table if not exists Publisher(PublisherID integer primary key autoincrement, PublisherName text)"
        genres = "create table if not exists Genre(GenreID integer primary key autoincrement, GenreName text unique)"
        orders = "create table if not exists Orders (OrderID integer primary key autoincrement, OrderAddress text, AppUserID integer, foreign key (AppUserID) references AppUser(AppUserID))"
        appusers = "create table if not exists AppUser(AppUserID integer primary key autoincrement, AppUserName " \
                   "text unique, Password text, Role text)"
        books = "create table if not exists Book(BookID integer primary key autoincrement, BookName text, Price number, WriterID integer,GenreID integer, PublisherID integer, foreign key (WriterID) references Writer(WriterID), foreign key (GenreID) references Genre(GenreID), foreign key (PublisherID) references Publisher(PublisherID))"
        orderDetails = "create table if not exists OrderDetails(OrderID integer, BookID integer, foreign key (OrderID) references Orders(OrderID), foreign key (BookID) references Book(BookID))"
        commands = [writers, publishers, genres, orders, appusers, books, orderDetails]
        for x in commands:
            self.__cursor.execute(x)
        self.__Connection.commit()

    def EndConnection(self):
        self.__Connection.close()

    def __init__(self):
        self.__CreateConnection()

    def ShowBooks(self):
        showBooks = "select BookID, BookName, Price from Book"
        self.__cursor.execute(showBooks)
        books = self.__cursor.fetchall()
        if (len(books) == 0):
            print("gösterilecek kitap bulunamadı")
        else:
            ##_bookName, _price, _writerID= None, _publisherID = None, _genreID= None, _bookID= None
            for x in books:
                bookobjects = Book(x[1], x[2], _writerID=None, _publisherID=None, _genreID=None, _bookID=x[0])
                print(bookobjects)

    def FindBooks(self, _bookName):
        findBooks = "select * from Book where BookName = ? "
        self.__cursor.execute(findBooks, (_bookName,))
        books = self.__cursor.fetchall()
        if (len(books) == 0):
            print("aradığınız kitap bulunamadı")
        else:
            bookobject = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            print(bookobject)

    def AddBook(self, book: Book):
        addbook = "insert into Book (BookName, Price, WriterID, PublisherID, GenreID) values (?,?,?)"
        self.__cursor.execute(addbook, (book.BookName, book.Price, book.WriterID, book.PublisherID, book.GenreID,))
        self.__Connection.commit()

    def FindBookID(self, _bookName):
        findBookID = "select BookID from Book where BookName = ? "
        self.__cursor.execute(findBookID, (_bookName,))
        book = self.__cursor.fetchall()
        if (len(book) == 0):
            print("kitap bulunamadı")
        else:
            return book[0][0]

    def GetBookByID(self, _ID):
        getbookbyID = "select BookName from Book where BookID=? "
        self.__cursor.execute(getbookbyID, (_ID,))
        book = self.__cursor.fetchall()
        if (len(book) == 0):
            print("kitap bulunamadı")
        else:
            return book[0][0]

    def DeleteBook(self, _bookName):
        toBeDeleted = self.FindBookID(_bookName)
        deletedBook = "delete from Book where BookID = ?"
        self.__cursor.execute(deletedBook, (toBeDeleted,))
        self.__Connection.commit()

    def UpdatedBook(self, _oldBookName, _newName, _newPrice, _newWriterID, _newPublisherID, _newGenreID):
        toBeUpdatedID = self.FindBookID(_oldBookName)
        updateBook = "update Book set BookName=?, Price=?, WriterID=?, PublisherID =?, GenreID=? where BookID=?"
        self.__cursor.execute(updateBook,
                              (_newName, _newPrice, _newWriterID, _newPublisherID, _newGenreID, toBeUpdatedID,))
        self.__Connection.commit()

    def ShowWriters(self):
        showWriters = "select WriterID, WriterName, WriterSurname from Writer"
        self.__cursor.execute(showWriters)
        writers = self.__cursor.fetchall()
        if (len(writers) == 0):
            print("yazar bulunamadı")
        else:
            for x in writers:
                writerobject = Writer(x[1], x[2], x[0])
                print(writerobject)

    def AddWriter(self, writer: Writer):
        insertWriter = "insert into Writer (WriterName, WriterSurname) values (?,?)"
        self.__cursor.execute(insertWriter, (writer.WriterName, writer.WriterSurname))
        self.__Connection.commit()

    def FindWriter(self, _writerSurname):
        findWriter = "select WriterID from Writer where WriterSurname =?"
        self.__cursor.execute(findWriter, (_writerSurname,))
        writer = self.__cursor.fetchall()
        if (len(writer) == 0):
            print("aradığınız yazar listede mevcut değil")
        else:
            for x in writer:
                return writer[0][0]

    def GetWriterByID(self, _ID):
        findWriter = "select WriterSurname from Writer where WriterID = ?"
        self.__cursor.execute(findWriter, (_ID,))
        writer = self.__cursor.fetchall()
        if (len(writer) == 0):
            print("aradığınız yazar listede mevcut değil")
        else:
            for x in writer:
                return writer[0][0]

    def DeleteWriter(self, _writerSurname):
        toBeDeleted = self.FindWriter(_writerSurname)
        deleteWriter = "delete from Writer where WriterID=?"
        self.__cursor.execute(deleteWriter, (toBeDeleted,))
        self.__Connection.commit()

    def UpdateWriter(self, _oldWriterSurname, _newName, _newSurname):
        toBeUpdatedID = self.FindWriter(_oldWriterSurname)
        updateWriter = "update Writer set WriterName=?, WriterSurname=? where WriterID =?"
        self.__cursor.execute(updateWriter, (_newName, _newSurname, toBeUpdatedID))
        self.__Connection.commit()

    def ShowPublishers(self):
        showPublishers = "select PublisherID, PublisherName from Publisher"
        self.__cursor.execute(showPublishers)
        publishers = self.__cursor.fetchall()
        if (len(publishers) == 0):
            print("yayınevi bulunamadı")
        else:
            for x in publishers:
                publisherobject = Publisher(x[1], x[0])
                print(publisherobject)

    def AddPublisher(self, publisher: Publisher):
        insertPublisher = "insert into Publisher (PublisherName) values (?)"
        self.__cursor.execute(insertPublisher, (publisher.PublisherName,))
        self.__Connection.commit()

    def FindPublisher(self, _publisherName):
        findPublisher = "select PublisherID from Publisher where PublisherName =?"
        self.__cursor.execute(findPublisher, (_publisherName,))
        publisher = self.__cursor.fetchall()
        if (len(publisher) == 0):
            print("aradığınız yayınevi listede mevcut değil")
        else:
            for x in publisher:
                return Publisher[0][0]

    def GetPublisherByID(self, _ID):
        findPublisher = "select PublisherName from Publisher where PublisherID = ?"
        self.__cursor.execute(findPublisher, (_ID,))
        publisher = self.__cursor.fetchall()
        if (len(publisher) == 0):
            print("aradığınız yayınevi listede mevcut değil")
        else:
            for x in publisher:
                return publisher[0][0]

    def DeletePublisher(self, _publisherName):
        toBeDeleted = self.FindPublisher(_publisherName)
        deletePublisher = "delete from Publisher where PublisherID=?"
        self.__cursor.execute(deletePublisher, (toBeDeleted,))
        self.__Connection.commit()

    def UpdatePublisher(self, _oldPublisherName, _newName):
        toBeUpdatedID = self.FindPublisher(_oldPublisherName)
        updatePublisher = "update Publisher set PublisherName=? where PublisherID =?"
        self.__cursor.execute(updatePublisher, (_newName, toBeUpdatedID))
        self.__Connection.commit()

    def ShowGenres(self):
        showGenres = "select GenreID, GenreName from Genre"
        self.__cursor.execute(showGenres)
        genres = self.__cursor.fetchall()
        if (len(genres) == 0):
            print("tür bulunamadı")
        else:
            for x in genres:
                genreobject = Genre(x[1], x[0])
                print(genreobject)

    def AddGenre(self, genre: Genre):
        insertGenre = "insert into Genre (GenreName) values (?)"
        self.__cursor.execute(insertGenre, (genre.GenreName,))
        self.__Connection.commit()

    def FindGenre(self, _genreName):
        findGenres = "select GenreID from Genre where GenreName =?"
        self.__cursor.execute(findGenres, (_genreName,))
        genres = self.__cursor.fetchall()
        if (len(genres) == 0):
            print("aradığınız tür listede mevcut değil")
        else:
            for x in genres:
                return Genre[0][0]

    def DeleteGenre(self, _genreID):
        deleteGenre = "delete from Genre where GenreID=?"
        self.__cursor.execute(deleteGenre, (_genreID,))
        self.__Connection.commit()

    def UpdateGenre(self, _oldGenreID, _newName):
        updateGenre = "update Genre set GenreName=? where GenreID =?"
        self.__cursor.execute(updateGenre, (_newName, _oldGenreID))
        self.__Connection.commit()

    def FindUserID(self, _username):
        findUserID = "select AppUserID from AppUser where AppUserName=?"
        self.__cursor.execute(findUserID, (_username,))
        kullanici = self.__cursor.fetchall()
        if (len(kullanici) == 0):
            print("kullanıcı bulunamadı")
        else:
            return kullanici[0][0]

    def FindUserRole(self, _username):
        findUserRole = "select Role from AppUser where AppUserName=?"
        self.__cursor.execute(findUserRole, (_username,))
        kullanici = self.__cursor.fetchall()
        if (len(kullanici) == 0):
            print("kullanıcı bulunamadı")
        else:
            return kullanici[0][0]

    def AddUser(self, user: AppUser):
        insertUser = "insert into AppUser (AppUserName, Password, Role) values (?,?,?)"
        self.__cursor.execute(insertUser, (user.AppUserName, user.Password, user.Role,))
        self.__Connection.commit()

    def ShowUser(self):
        showUser = "select UserName, Password, Role from AppUser"
        self.__cursor.execute(showUser)
        users = self.__cursor.fetchall()
        if (len(users) == 0):
            print("kullanıcı bulunmamaktadır")
        else:
            for x in users:
                u = AppUser(x[0], x[1], x[2])
                print(u)

    def DeleteAppUser(self, _appUserID):
        toBeUpdatedID = self.FindUserID(_appUserID)
        deleteUser = "delete from AppUser where AppUserID=?"
        self.__cursor.execute(deleteUser, (toBeUpdatedID,))
        self.__Connection.commit()

    def UpdateAppUser(self, _oldAppUserName, _newPassword, _newRole):
        toBeUpdatedID = self.FindUserID(_oldAppUserName)
        updateUser = "update AppUser set Password=?, Role=? where AppUserID =?"
        self.__cursor.execute(updateUser, (_newPassword, _newRole, toBeUpdatedID))
        self.__Connection.commit()

    def AddOrder(self, order: Order):
        insertOrder = "insert into Order (ShippedAddress) values (?)"
        self.__cursor.execute(insertOrder, (order.ShippedAddress,))
        self.__Connection.commit()

    def FindOrderID(self):
        findOrderID = "select OrderID from Order order by OrderID desc limit 1"
        self.__cursor.execute(findOrderID)
        order = self.__cursor.fetchall()
        if (len(order) == 0):
            print("sipariş bulunmamaktadır")
        else:
            return order[0][0]

    def DeleteOrder(self, _orderID):
        deleteOrder = "delete from Order where OrderID=?"
        self.__cursor.execute(deleteOrder, (_orderID, ))
        self.__Connection.commit()

    def AddOrderDetails(self, orderDetails: OrderDetails):
        inserOrderDetails = "insert into OrderDetails (OrderID, BookID) values (?,?)"
        self.__cursor.execute(inserOrderDetails, (orderDetails.OrderID, orderDetails.BookID,))
        self.__Connection.commit()


