package main

import (
	"database/sql"
	"fmt"
	"io"
	"log"
	"net"
	"strings"
	"time"

	_ "github.com/mattn/go-sqlite3"
)

func errHandler(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

var (
	db,db2 *sql.DB
	tx, tx2 *sql.Tx
	stmt, stmt2 *sql.Stmt
)

func main() {
	l, err := net.Listen("tcp", ":30122")
	if nil != err {
		fmt.Print("fial to bind address", err)
		return
	}
	defer l.Close()
	db, err = sql.Open("sqlite3", "./pmdata.db")
	errHandler(err)
	defer db.Close()
	db2, err = sql.Open("sqlite3", "./humdata.db")
	errHandler(err)
	defer db2.Close()
	tx, err = db.Begin()
	errHandler(err)
	tx2, err = db2.Begin()
	errHandler(err)
	stmt, err = tx.Prepare("insert into data(pm10,pm25,time) values (?,?,?)")
	errHandler(err)
	defer stmt.Close()
	stmt2, err = tx2.Prepare("insert into hum(hum,tem,time) values (?,?,?)")
	errHandler(err)
	defer stmt2.Close()

	for {
		conn, err := l.Accept()
		if nil != err {
			log.Printf("fail to accept; err : %v", err)
			continue
		}

		go ConnHandler(conn)
	}
}

// ConnHandler input db receved data
func ConnHandler(conn net.Conn) {
	recvBuf := make([]byte, 256)
	ok := []byte{'o', 'k'}
	for {
		n, err := conn.Read(recvBuf)
		if nil != err {
			if io.EOF == err {
				log.Printf("connection is closed from client; %v", conn.RemoteAddr().String())
				return
			}
			log.Printf("fail to receive data; err: %v", err)
			return
		}
		if 0 < n {
			// pm10 pm25 hum tem time
			recv := recvBuf[:n]
			data := string(recv)
			fmt.Println(data)
			conn.Write(ok)
			datas := strings.Split(data, " ")
			Time := datas[4]+ " " + datas[5]
			stmt.Exec(datas[0], datas[1], Time)
			stmt2.Exec(datas[2], datas[3], Time)
			tx.Commit()
			tx2.Commit()
		}
	}
}
