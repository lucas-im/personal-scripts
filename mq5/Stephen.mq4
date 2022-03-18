//+------------------------------------------------------------------+
//|                                                      Stephen.mq4 |
//|                                         Ko Naing, ForexEAService |
//|                            https://www.facebook.com/konaingforex |
//+------------------------------------------------------------------+
#property copyright "Ko Naing, ForexEAService"
#property link      "https://www.facebook.com/konaingforex"
#property version   "1.00"
#property strict

    enum day
  {
   on   =  0,        // On
   off   =  1,      // OFF
  };
  
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
extern   string            st1            = "System 1 Settings";        // System 1 Settings
extern   bool              syst1          = true;                      // Use System 1
extern   string           setTime         =  "00:05:00";               // Lefit Time  (HH:MM:SS)
extern   day                  day1           =  1;                         // Time Trade
extern   string               startTime      = "00:00";                    // Start Time
extern   string               endTemie       = "15:59";                    // End Time
extern   double           lot             =0.1;                        // Lot
extern   double           multiply        = 2;                         // Lot Multiply
extern   double           pipstep         = 200;                       //  Pipstep
extern   double           tp              = 100;                       // TP
extern   double           sl              = 0;                       // SL
extern   int              max             = 6;                          // Max Trade
extern   string            st2            = "System 2 Settings";        // System 2 Settings
extern   day                  day2        =  1;                         // Time Trade
extern   string               startTime2  = "23:00";                    // Start Time
extern   string               endTemie2   = "23:59";                    // End Time
extern   bool              syst2          = false;                      // Use System 2
extern   double           lot2            =0.1;                        // Lot
extern   double           multiply2       = 2;                         // Lot Multiply
extern   double           pipstep2        = 200;                       //  Pipstep
extern   double           tp2             = 100;                       // TP
extern   double           sl2             = 100;                       // SL
extern   int              magic           = 2021;                     // Magic Number;
datetime leftTime=0;
int magic2=0;

#define st "ST"
#define ExpertName _Symbol
#resource "\\Include\\Controls\\res\\DropOn.bmp"
#resource "\\Include\\Controls\\res\\DropOff.bmp"
#define All 10
color  C5   = C'030,255,000';
color c1 = C'60,103,135';
int mainX=10;
int mainY=200;
int mainXsize =800;
int mainYsize=430;
string comment[],comment2[];


// ======== USER CONTROL PANNEL ================

string   EaName   =  "Stephen EA";            // EA Name

string com="ST EA";

int ACC=2   ;// Account Number  {  ACC=1 Demo only // ACC=2 No security // ACC= 14529843 Only Noumber Account }

string AC_Name=" ";

datetime Exp=D'2121.12.18';


//===================================================
double  blot,mlot;
datetime time1,time2 , time3, time4;
bool modify;
int ary=1,ary2=1;
int OnInit()
  {
//--- create timer
   EventSetMillisecondTimer(100);


   if(AccountName()!=AC_Name && AC_Name!=" ")
     {
      Alert("Wrong account Name!  "+" This is version for "+AC_Name);
      ExpertRemove();
     }
   if(AC_Name==" " && ACC==1 && IsDemo()==false)
     {
      Alert("This is Demo version for Demo accounts only!");
      ExpertRemove();
     }

   if(AC_Name==" " && ACC!=1 && ACC!=AccountNumber() && ACC!=2)
     {
      Alert("Wrong account number!");
      ExpertRemove();
     }

   if(TimeCurrent()>Exp)
     {
      Alert(" Working Date is Expired !");
      ExpertRemove();
     }

   if(lot<MarketInfo(_Symbol,MODE_MINLOT))
     {
      blot =MarketInfo(_Symbol,MODE_MINLOT);
     }
   else
     {
      blot=lot;
     }
   mlot=blot;
   magic2=magic*2;
   ArrayResize(comment,ary);
     ArrayResize(comment2,ary2);
     time3=iTime(_Symbol,0,0);
     time4=iTime(_Symbol,0,0);
//---
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//--- destroy timer
   EventKillTimer();
    for(int i=ObjectsTotal()-1; i>=0; i--)
     {
      string label=ObjectName(i);
      if(StringSubstr(label,0,StringLen(st))!=st)
         continue;
      ObjectDelete(label);
     }


   ObjectDelete("Back");
   ObjectDelete("Y");
   ObjectDelete("001");
   ObjectDelete("002");
   ObjectDelete("swPANNEL");

  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//---
   if(IsTesting())
     {
      OnTimer();

     }

  }
//+------------------------------------------------------------------+
//| Timer function                                                   |
//+------------------------------------------------------------------+
void OnTimer()
  {
   leftTime = leftTime();
//---

int x=0;
 
   Create_OBJ("Back",OBJ_RECTANGLE_LABEL,0,x,0,220,50);
   Create_OBJ("Y",OBJ_RECTANGLE_LABEL,0,x,45,220,7,clrPaleGreen);
   Create_OBJ("001",OBJ_LABEL,0,x+14,15);
   ObjectSetText("001",EaName,12,"Arial Black",clrPaleGoldenrod);
   Create_OBJ("002",OBJ_LABEL,0,x+142,20);
   ObjectSetText("002",_Symbol,9,"Arial Bold",White);
   Create_OBJ("sw"+"PANNEL",OBJ_BITMAP_LABEL,0,x+200,30);

   if(ObjectGetInteger(0,"sw"+"PANNEL",OBJPROP_STATE)==0)// on
     {
      Create_OBJ(st+"Back",OBJ_RECTANGLE_LABEL,0,x,50,220,180);
      ObjectSetString(0,"sw"+"PANNEL",OBJPROP_BMPFILE,0,"::Include\\Controls\\res\\DropOn.bmp");
      Create_OBJ(st+"003",OBJ_LABEL,0,x+14,60);

      Create_OBJ(st+"004",OBJ_LABEL,0,x+14,80);

      Create_OBJ(st+"005",OBJ_LABEL,0,x+14,100);

      Create_OBJ(st+"006",OBJ_LABEL,0,x+14,120);

      Create_OBJ(st+"007",OBJ_LABEL,0,x+14,140);
      
      Create_OBJ(st+"008",OBJ_LABEL,0,x+14,160);
      
      Create_OBJ(st+"012",OBJ_LABEL,0,x+15,180);
      
      Create_OBJ(st+"014",OBJ_LABEL,0,x+15,200);
       
      ObjectSetText(st+"003","System 1 Buy    : "+IntegerToString(total(OP_BUY,magic)),8,"Arial Black",clrDodgerBlue);

      ObjectSetText(st+"004","System 1 Sell    : "+IntegerToString(total(OP_SELL,magic)),8,"Arial Black",clrRed);

      ObjectSetText(st+"005","System 1 Profit : "+DoubleToString(profit(All,0,magic),0),8,"Arial Black",pfColor(profit(All,0,magic)));
      
      
      ObjectSetText(st+"006","System 2 Buy    : "+IntegerToString(total(OP_BUY,magic2)),8,"Arial Black",clrCyan);

      ObjectSetText(st+"007","System 2 Sell    : "+IntegerToString(total(OP_SELL,magic2)),8,"Arial Black",clrPaleVioletRed);

      ObjectSetText(st+"008","System 2 Profit  : "+DoubleToString(profit(All,0,magic2),0),8,"Arial Black",pfColor(profit(All,0,magic2)));

   ObjectSetText(st+"012","Server Time   : "+TimeToString(TimeCurrent(),TIME_MINUTES|TIME_SECONDS)+"",8,"Arial Black",White);    
   ObjectSetText(st+"014","Time Left       : "+(string)leftDay()+"D "+toString(leftTime),8,"Arial Black",White);

     

     }


   else
      if(ObjectGetInteger(0,"sw"+"PANNEL",OBJPROP_STATE)==1)// off
        {

         for(int i=0; i<ObjectsTotal(); i++)
           {
            //-- GetObjectName
            string obj_name=ObjectName(i);
            //-- PrefixObjectFound
            if(StringSubstr(obj_name,0,StringLen(st))==st)
              {
               //-- DeleteObjects
               if(ObjectsDeleteAll(0,st,-1,-1)>0)
                  break;
              }
           }

         ObjectSetString(0,"sw"+"PANNEL",OBJPROP_BMPFILE,0,"::Include\\Controls\\res\\DropOff.bmp");


        }

   if(total(10,magic)<1)
     {
      ArrayResize(comment,1);
      ary=1;
     }
     if(total(10,magic2)<1)
     {
      ArrayResize(comment2,1);
      ary2=1;
     }
   if(ary>0)
     {

      for(int a=ArraySize(comment); a>0; a--)
        {
         if(lastCom(OP_BUY,magic)==comment[a-1])
           {
            close(OP_BUYLIMIT,magic,comment[a-1]);
            close(OP_BUY,magic,comment[a-1]);
           }

         if(totalPending(OP_SELL,magic,comment[a-1])<1 &&lastCom(OP_SELL,magic)==comment[a-1])
           {
            close(OP_SELLLIMIT,magic,comment[a-1]);
            close(OP_SELL,magic,comment[a-1]);
           }

         if(pipStep(OP_BUY,magic,comment[a-1],pipstep)&& totalPending(OP_BUY,magic,comment[a-1])>0&&  total(OP_BUY,magic)<max)
           {
            if(orderSend(OP_BUY,lotmode(OP_BUY,magic,comment[a-1],multiply),Ask,0,tp,StringSubstr(comment[a-1],StringLen(com+" "),0),magic,clrCyan))
            {
            martin(OP_BUY,magic,comment[a-1]);
            }
           }

         if(pipStep(OP_SELL,magic,comment[a-1],pipstep)&& totalPending(OP_SELL,magic,comment[a-1])>0 && total(OP_SELL,magic)<max)
           {
            if(orderSend(OP_SELL,lotmode(OP_SELL,magic,comment[a-1],multiply),Bid,0,tp,StringSubstr(comment[a-1],StringLen(com+" "),0),magic,clrMagenta)){
            martin(OP_SELL,magic,comment[a-1]);
            }
           }
        }

     }
     
     
        if(ary2>0)
     {

      for(int a=ArraySize(comment2); a>0; a--)
        {
             

         if(pipStep(OP_BUY,magic2,comment2[a-1],pipstep2)&& totalPending(OP_BUY,magic2,comment2[a-1])>0&&  total(OP_BUY,magic2)<max)
           {
           
            if(orderSend(OP_BUY,lotmode(OP_BUY,magic2,comment2[a-1],multiply2),Ask,0,tp2,StringSubstr(comment2[a-1],StringLen(com+" "),0),magic2,clrCyan))
            {
            martin(OP_BUY,magic2,comment2[a-1]);
            }
           }

         if(pipStep(OP_SELL,magic2,comment2[a-1],pipstep2)&& totalPending(OP_SELL,magic2,comment2[a-1])>0 && total(OP_SELL,magic2)<max)
           {
            if(orderSend(OP_SELL,lotmode(OP_SELL,magic2,comment2[a-1],multiply2),Bid,0,tp2,StringSubstr(comment2[a-1],StringLen(com+" "),0),magic2,clrMagenta)){
            martin(OP_SELL,magic2,comment2[a-1]);
            }
           }
        }

     }
//   Comment(" System 1 Profit "+DoubleToStr(profit(10,0,magic),2)
//            +"\n System 1 BUY Total "+total(OP_BUY,magic)
//           +"\n System 1 SELL Total "+total(OP_SELL,magic)
//           +"\nTime Left "+(string)leftDay()+" Days "+toString(leftTime)
//         
//           +"\n  System 2 Profit "+DoubleToStr(profit(10,0,magic2),2)
//           +"\n System 2 BUY Total "+total(OP_BUY,magic2)
//           +"\n System 2 SELL Total "+total(OP_SELL,magic2)
//           
//
////  +"\n Array "+(string)ArraySize(comment)
//
//
//
//          );


   if(onBar(time1)&&timeChk(startTime,endTemie,day1)&&total(OP_BUY,magic)<max &&syst1&& leftDay()==0&&toString(leftTime)==setTime && Open[0]>Close[0])
     {
      string tm=TimeToStr(TimeCurrent(),TIME_DATE|TIME_MINUTES);
      if(orderSend(OP_BUY,mlot,Ask,sl,tp,tm+"S1B",magic,clrBlue))
        {

        // orderSend(OP_BUYLIMIT,lotmode(OP_BUY,magic,com+" "+tm+"S1B"),Ask-pipstep*Point(),0,lmTp,tm+"S1B",magic,clrCyan);
         time1=iTime(_Symbol,0,0);
         ArrayResize(comment,ary);
         comment[ary-1]=com+" "+tm+"S1B";
         ary++;
        }
     }



   if(onBar(time2)&&timeChk(startTime,endTemie,day1)&&total(OP_SELL,magic)<max&&syst1&&leftDay()==0&&toString(leftTime)==setTime && Open[0]<Close[0])
     {
      string tm=TimeToStr(TimeCurrent(),TIME_DATE|TIME_MINUTES);
      if(orderSend(OP_SELL,mlot,Bid,sl,tp,tm+"S1S",magic,clrRed))
        {
        // orderSend(OP_SELLLIMIT,lotmode(OP_SELL,magic,com+" "+tm+"S1S"),Bid+pipstep*Point(),0,lmTp,tm+"S1S",magic,clrMagenta);
         time2=iTime(_Symbol,0,0);
         ArrayResize(comment,ary);
         comment[ary-1]=com+" "+tm+"S1S";
         ary++;
        }
     }
     
     

//-
   if(syst2&&onBar(time3)&&timeChk(startTime2,endTemie2,day2)&&total(OP_BUY,magic2)<max && Open[2]>Close[2]&& Open[1]>Close[1])
     {
         string tm=TimeToStr(TimeCurrent(),TIME_DATE|TIME_MINUTES);
         orderSend(OP_BUY,lot2,Ask,sl2,tp2,tm+"S2B",magic2,clrBlue);
         ArrayResize(comment2,ary2);
         comment2[ary2-1]=com+" "+tm+"S2B";
         ary2++;
         time3=iTime(_Symbol,0,0);
     }

   if(syst2&&onBar(time4)&&timeChk(startTime2,endTemie2,day2)&&total(OP_SELL,magic2)<max && Open[2]<Close[2]&& Open[1]<Close[1])
     {
         string tm=TimeToStr(TimeCurrent(),TIME_DATE|TIME_MINUTES);
         orderSend(OP_SELL,lot2,Bid,sl2,tp2,tm+"S2S",magic2,clrRed);
         ArrayResize(comment2,ary2);
         comment2[ary2-1]=com+" "+tm+"S2S";
         ary2++;
         time4=iTime(_Symbol,0,0);
     }

//-



  }
//+------------------------------------------------------------------+

void martin (int OP_,int mag,string cm){

      double OPrice=0;
      double OLot=0;
      double   TP_Price=0;
      double   SL_Price=0;
      for(int i=OrdersTotal()-1; i>=0; i--)
      {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
        if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag && OrderComment()==cm)
      if (OrderType()==OP_)
      {
       OPrice+=OrderOpenPrice()*OrderLots(); //  OPrice= OPrice+OrderOpenPrice()*OrderLots();
       OLot+=OrderLots();
      }
      }
      if (totalPending(OP_,mag,cm)>1)
      {OPrice=NormalizeDouble(OPrice/OLot,Digits);
     
     
      for(int i=OrdersTotal()-1; i>=0; i--)
      {
      int ret0=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
        if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag && OrderComment()==cm)
      if (OrderType()==OP_&& OP_==OP_BUY)
      {
      if(tp!=0)
      {TP_Price=OPrice+tp*Point;}
      else if(tp==0)
      {TP_Price=tp;}
      
      }
     
      
      }
      
      
      for(int i=OrdersTotal()-1; i>=0; i--)
      {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
        if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag && OrderComment()==cm)
      if (OrderType()==OP_&& OP_==OP_SELL)
      {
      if(tp!=0)
      {TP_Price=OPrice-tp*Point;}
      else if(tp==0)
      {TP_Price=tp;}
    
      }
     
      
      }
      
      
      }
      
      
       for(int i=OrdersTotal()-1; i>=0; i--)
      {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
       if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag && OrderComment()==cm)
      int ret2=OrderModify(OrderTicket(),OPrice,SL_Price,TP_Price,0,clrAntiqueWhite);
      

}
}
//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double lastMoment(int OP_,string moment,int mag)
  {
   double otp=0;
   double ocp=0;
   double osl=0;
   double opf=0;
   double mm=0;

   for(int i=0; OrdersHistoryTotal()>i; i++)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_HISTORY);

      if(OrderSymbol()!=Symbol()||OrderMagicNumber()!=mag || OrderType()>1)
         continue;
      if(OrderSymbol()==Symbol()&&OrderMagicNumber()==mag && OrderType()<2)
         if(OrderType()==OP_||OP_==10)

           {
            if(OrderCloseTime()>=iTime(Symbol(),PERIOD_M1,0))
              {
               otp=OrderTakeProfit();
               osl=OrderStopLoss();
               ocp=OrderClosePrice();
               opf=OrderProfit()+OrderSwap()+OrderCommission();

              }
           }


     }
   if(moment=="otp")
     {
      mm=otp;
     }

   if(moment=="ocp")
     {
      mm=ocp;
     }
   if(moment=="osl")
     {
      mm=osl;
     }
   if(moment=="opf")
     {
      mm=opf;
     }
   return(mm);
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
string lastCom(int OP_,int mag)
  {

   string mm="";

   for(int i=0; OrdersHistoryTotal()>i; i++)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_HISTORY);

      if(OrderSymbol()!=Symbol()||OrderMagicNumber()!=mag || OrderType()>1)
         continue;
      if(OrderSymbol()==Symbol()&&OrderMagicNumber()==mag && OrderType()<2)
         if(OrderType()==OP_||OP_==10)

           {
            if(OrderClosePrice()==OrderTakeProfit()&&OrderCloseTime()>=iTime(Symbol(),PERIOD_M1,0))
              {
               mm= StringSubstr(OrderComment(),0,StringLen(com+" "+TimeToStr(TimeCurrent(),TIME_DATE|TIME_MINUTES)+"S1S"));
              }
           }


     }


   return(mm);
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double profit(int OP_, int  mo = 0,int mag=0)
  {
   double profit=0;

   for(int i=OrdersTotal()-1; i>=0; i--)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag)
         if(OrderType()==OP_||OP_==10)
           {
            if(mo==0)
              {
               profit+=OrderProfit()+OrderSwap()+OrderCommission();
              }
            else
              {
               profit+=OrderLots();
              }
           }
     }
   return(profit);
  }
//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
datetime leftTime()
  {
   return (Period()*60)-(TimeCurrent()-Time[0]);
  }
//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
string toString(datetime time)
  {
   return TimeToStr(time,TIME_SECONDS);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
int leftDay()
  {
   int days=0;
   if(Period()==PERIOD_MN1 || Period()==PERIOD_W1)
     {
      days=(int)((leftTime()/60)/60)/24;
     }
   return  days;
  }
//+------------------------------------------------------------------+
bool orderSend(int _op, double _lot,double _price,  double _sl,double _tp, string cm,int mag,color _cl= clrNONE)
  {

   double SL=0,TP=0;

   if(_op==OP_BUY)
     {

      if(_sl!=0)
        {
         SL=_price-_sl*Point();
        }
      if(_tp!=0)
        {
         TP=_price+_tp*Point();
        }

     }

   if(_op==OP_BUYLIMIT)
     {

      if(_sl!=0)
        {
         SL=_price-_sl*Point();
        }
      if(_tp!=0)
        {
         TP=_price+_tp*Point();
        }


     }

   if(_op==OP_SELL)
     {

      if(_sl!=0)
        {
         SL=_price+_sl*Point();
        }
      if(_tp!=0)
        {
         TP=_price-_tp*Point();
        }

     }

   if(_op==OP_SELLLIMIT)
     {

      if(_sl!=0)
        {
         SL=_price+_sl*Point();
        }
      if(_tp!=0)
        {
         TP=_price-_tp*Point();
        }


     }
   return (bool) OrderSend(_Symbol,_op,_lot,_price,3,SL,TP,com+" "+cm,mag,0,_cl);


  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
int total(int OP=10,  int mag = 0)
  {
   int Cont=0;
   for(int i=OrdersTotal()-1; i>=0; i--)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol()!=Symbol() || OrderMagicNumber()!=mag)
         continue;
      if(OrderSymbol()==Symbol() && OrderMagicNumber()==mag)
         if(OrderType()==OP||OP==10)
            Cont++;
     }
   return(Cont);
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool pipStep(int OP_,int mag,string cm,double EntryPip)
  {

   if(OP_==OP_BUY && lastPrice(OP_,mag,cm)-EntryPip*Point>Ask)
     {
      return true;
     }
   else
      if(OP_==OP_SELL && lastPrice(OP_,mag,cm)+EntryPip*Point<Bid)
        {
         return true;
        }
      else
         return false;

  }
//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool onBar(datetime date)
  {
   return (date!=Time[0]);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double lotmode(int OP_,int mag,string cm, double multy)
  {
   double l=0;

   if(totalPending(OP_,mag,cm)>0)
     {
      l=lastLot(OP_,mag,cm)*multy;
     }
   else
     {
      l=mlot;
     }


   return l;
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void close(int OP_,int mag,string cm)
  {
   for(int i=OrdersTotal()-1; i>=0; i--)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag && OrderComment()==cm)

         if((OrderType()==OP_||OP_==10) &&OrderType()<2)
           {

            int ret1=OrderClose(OrderTicket(),OrderLots(),OrderClosePrice(),30,clrWhite);
           }
         else
            if((OrderType()==OP_||OP_==10)&&OrderType()>1)
              {
               int re = OrderDelete(OrderTicket(),clrNONE);

              }
     }
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void closePending(int OP_,int mag,string cm)
  {
   for(int i=OrdersTotal()-1; i>=0; i--)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag && OrderComment()==cm)

         if(OrderType()==OP_)
           {
            int re = OrderDelete(OrderTicket(),clrNONE);

           }
     }
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
int totalPending(int OP=10,  int mag = 0, string cm=" ")
  {
   int Cont=0;
   for(int i=OrdersTotal()-1; i>=0; i--)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol()!=_Symbol || OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol && OrderMagicNumber()==mag && OrderComment()==cm)
         if(OrderType()==OP||OP==10)
            Cont++;
     }
   return(Cont);
  }
//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double lastLot(int OP,  int mag, string cm)
  {
   int tick=0;
   int tick1=0;
   double l=0;

   for(int i=OrdersTotal(); i>=0; i--)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol()!=_Symbol || OrderType()!=OP||OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol &&OrderType()==OP&& OrderMagicNumber()==mag && OrderComment()==cm)

         tick=OrderTicket();
      if(tick>tick1)
        {
         l=OrderLots();
         tick1=tick;

        }
     }
   return(l);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double lastPrice(int OP,int mag,string cm)
  {
   double price=0;

   int tick=0;
   int tick1=0;
   for(int i=OrdersTotal()-1; i>=0; i--)
     {
      int ret=OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol()!=_Symbol || OrderType()!=OP||OrderMagicNumber()!=mag|| OrderComment()!=cm)
         continue;
      if(OrderSymbol()==_Symbol &&OrderType()==OP&& OrderMagicNumber()==mag && OrderComment()==cm)
         
            tick=OrderTicket();
      if(tick>tick1)
        {
         price=OrderOpenPrice();
         tick1=tick;   

        }
     }
   return(price);
  }
//+------------------------------------------------------------------+
 bool timeChk(string stTime, string enTime, day dc)
  {
   bool td = false;

   if(dc==0 && TimeCurrent()>=StrToTime(stTime)&&TimeCurrent()<=StrToTime(enTime))
      {td=true;}
          else if(dc==1){
         td=true;}
   return(td);
  }
  
  
  //+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
color pfColor(double profit)
  {

   if(profit>0)
     {

      return clrGreenYellow;
     }
   else
      if(profit<0)
        {
         return clrRed;
        }

   return clrGray;

  }
  void Create_OBJ(string Name="",
                ENUM_OBJECT Type=0,
                int CORNER =0,
                int XDISTANCE=0,
                int YDISTANCE=0,
                int XSIZE=0,
                int YSIZE=0,
                color BGCOLOR=C'025,025,025',
                color OBJ_COLOR=C'000,000,000',
                string TEXT="",
                int    font_size=10,
                string font="Arial"

               )

  {
   if(ObjectFind(Name)!=0)
     {
      ObjectCreate(Name,Type,0,0,0);
      ObjectSet(Name,OBJPROP_CORNER,CORNER);
      ObjectSet(Name,OBJPROP_XDISTANCE,XDISTANCE);
      ObjectSet(Name,OBJPROP_YDISTANCE,YDISTANCE);
      ObjectSet(Name,OBJPROP_XSIZE,XSIZE);
      ObjectSet(Name,OBJPROP_YSIZE,YSIZE);
      ObjectSet(Name,OBJPROP_BGCOLOR,BGCOLOR);
      ObjectSet(Name,OBJPROP_COLOR,OBJ_COLOR);
      ObjectSetString(0,Name,OBJPROP_TEXT,TEXT);
      ObjectSetString(0,Name,OBJPROP_FONT,font);
      ObjectSet(Name,OBJPROP_FONTSIZE,font_size);
      ObjectSet(Name,OBJPROP_SELECTABLE,false);
      ObjectSet(Name,OBJPROP_SELECTED,false);
      ObjectSet(Name,OBJPROP_ZORDER,false);
      ObjectSetString(0,Name,OBJPROP_TOOLTIP,"\n");
      ObjectSet(Name,OBJPROP_ALIGN,ALIGN_CENTER);
      ObjectSet(Name,OBJPROP_SELECTED,false);
      ObjectSet(Name,OBJPROP_HIDDEN,true);
      ObjectSet(Name,OBJPROP_BORDER_TYPE,OBJPROP_FILL);
     }
  }
//+------------------------------------------------------------------+

//+------------------------------------------------------------------+