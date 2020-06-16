package main

import (
	"log"
	"net"
)

func main() {
	l, err := net.Listen("tcp", "30122")
	if nil != err {
		log.Fatalf("fial to bind address", err)
	}
	defer l.Close()

	for {
		conn, err := l.Accept()
		if nil != err {
			log.Printf("fail to accept; err : %v", err)
			continue
		}

		go ConnHandler(conn)
	}
}

func ConnHandler(conn net.Conn) {
	recvBuf := make([]byte, 256)
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
					data := recvBuf[:n]
					log.Println(string(data))
			}
	}
}