from src.share import loadingmsg
from time import sleep

def exit():
    print()
    sleep(2)
    loadingmsg("Exiting")
    print('{:^120s}'.format("*"*120))
    print()
    print('{:^120s}'.format("Terima kasih telah bermain!"))
    print('{:^120s}'.format("""
      SSS   eeee   eeee    yy   yy   ooo     uu   uu       a    gg gg   eeee  nn   nn   ttt
     S      e      e        yy yy  oo  oo    uu   uu      a a   g       e     nnn  nn    t
      SSS   eeee   eeee      yyy   oo  oo    uu   uu     aaaaa  g  gg   eee   nn n nn    t
         S  e      e          y    oo  oo    uu   uu     a   a  g   g   e     nn  nnn    t
      SSS   eeee   eeee       y     ooo      uuu uuu     a   a   gg g   eeee  nn   nn    t
    """))
    print('{:^120s}'.format("*"*120))
    
