# Generador de la Figura 1 — Flujo metodológico del Análisis del Dato.
# Se mantiene FUERA del notebook (igual que el diagrama ETL de la Ingeniería del Dato)
# para que el cuaderno se centre en el análisis. Regenera figuras/Analisis_Fig01_flujo_metodologico.png.
# Ejecutar:  python generar_diagrama_flujo_analisis.py
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
FIG_DIR = Path(__file__).resolve().parent / "figuras"
FIG_DIR.mkdir(exist_ok=True)
def display(*a, **k):
    pass  # no-op fuera del notebook

# Figura 1 — Flujo metodológico del Análisis del Dato (trazable a las secciones del cuaderno)
import matplotlib.patches as mpatches
fig,ax=plt.subplots(figsize=(16,12.2)); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
BLUE='#23416e'; GREEN='#2e8b57'; SLATE='#5a4a7a'; WIN='#d8f0e0'; OUT='#eaf4ec'; GREY='#eef0f2'; MET='#e3ecfa'
SECF='#eceef0'; SECE='#aab0b8'; SECT='#5a6068'; AMBF='#fcf4d6'; AMBE='#d8c06a'; AMBT='#7a5a12'
def rbox(xc,w,top,h,t,fc,ec,bold,fs,tc='#1a1a1a',lw=1.25,asp=0.7):
    ax.add_patch(mpatches.FancyBboxPatch((xc-w/2,top-h),w,h,boxstyle='round,pad=0.18',fc=fc,ec=ec,lw=lw,zorder=3,mutation_aspect=asp)); ax.text(xc,top-h/2,t,ha='center',va='center',fontsize=fs,fontweight='bold' if bold else 'normal',color=tc,zorder=4)
def pw(t,fs): return len(t)*fs*0.048+1.2
def pill(x,y,t,fc,ec,tc,fs=6.1,h=1.5):
    w=pw(t,fs); ax.add_patch(mpatches.FancyBboxPatch((x,y-h/2),w,h,boxstyle='round,pad=0.05,rounding_size=0.8',fc=fc,ec=ec,lw=1.0,zorder=6,mutation_aspect=0.42)); ax.text(x+w/2,y,t,ha='center',va='center',fontsize=fs,fontweight='bold',color=tc,zorder=7); return w
def cpill(xc,y,t,fc,ec,tc,fs=6.1): pill(xc-pw(t,fs)/2,y,t,fc,ec,tc,fs)
def pair(xL,y,sec,ref):
    w=pill(xL,y,sec,SECF,SECE,SECT); pill(xL+w+1.2,y,ref,AMBF,AMBE,AMBT)
def seqline(xc,y,segs,fs=7.0,tcol='#888'):
    cw=fs*0.057
    def wseg(s):
        k,t=s; return len(t)*cw if k=='t' else pw(t,fs-0.3)
    total=sum(wseg(s) for s in segs)+(len(segs)-1)*0.4; x=xc-total/2
    for s in segs:
        k,t=s; w=wseg(s)
        if k=='t': ax.text(x,y,t,ha='left',va='center',fontsize=fs,color=tcol,zorder=4)
        elif k=='s': pill(x,y,t,SECF,SECE,SECT,fs=fs-0.3)
        else: pill(x,y,t,AMBF,AMBE,AMBT,fs=fs-0.3)
        x+=w+0.4
def col(xc,w,ytop,steps,ec,headfc,step=7.0,h=5.0):
    tops=[]
    for i,(t,k) in enumerate(steps):
        top=ytop-i*step
        if   k=='head': fc,bold,tc,fs=headfc,True,BLUE,7.2
        elif k=='metric':fc,bold,tc,fs=MET,True,BLUE,7.6
        elif k=='out':  fc,bold,tc,fs=OUT,True,'#1d5c3a',7.4
        else:           fc,bold,tc,fs='white',False,'#1a1a1a',6.9
        rbox(xc,w,top,h,t,fc,GREEN if k=='out' else ec,bold,fs,tc)
        if i>0: ax.annotate('',xy=(xc,top),xytext=(xc,tops[-1]-h),arrowprops=dict(arrowstyle='-|>',color='#777',lw=1.1),zorder=2)
        tops.append(top)
    return tops[-1]-h
ax.text(50,97.6,'ANÁLISIS DEL DATO · Flujo metodológico',ha='center',fontsize=16,fontweight='bold',color=BLUE)
ax.text(50,94.5,'TFG — Desequilibrio entre alquiler y salario joven en España (2011-2024) · panel provincial 48×14 = 672 obs · 624 de modelado (sin 2011)',ha='center',fontsize=8,color='#555',style='italic')
# Caja esquina superior derecha: secciones de partida
ax.add_patch(mpatches.FancyBboxPatch((83.5,94.6),14.0,4.0,boxstyle='round,pad=0.16',fc='#f7f8fa',ec='#c4cad2',lw=1.0,zorder=3,mutation_aspect=0.5))
seqline(90.5,97.4,[('t','Punto de partida')],fs=5.9,tcol='#777')
seqline(90.5,95.7,[('t','Marco teórico')],fs=5.9,tcol='#777')
def qbox(xc,w,t):
    ax.add_patch(mpatches.FancyBboxPatch((xc-w/2,89.9),w,2.9,boxstyle='round,pad=0.2',fc='#f2f6fc',ec='#b9c7da',lw=1.2,zorder=3,mutation_aspect=0.6)); ax.text(xc,91.35,t,ha='center',va='center',fontsize=7.6,fontweight='bold',style='italic',color='#2a2a2a',zorder=4)
qbox(30.5,55,'¿Qué determina el alquiler y, por tanto, el esfuerzo?'); qbox(69.5,19,'¿Cómo se agrupan\nlas provincias?'); qbox(89.5,17,'¿Hacia dónde\nevoluciona el esfuerzo?')
def band(x0,x1,t,c):
    ax.add_patch(mpatches.FancyBboxPatch((x0,85.9),x1-x0,2.9,boxstyle='round,pad=0.2',fc=c,ec='none',zorder=2,mutation_aspect=0.6)); ax.text((x0+x1)/2,87.35,t,ha='center',va='center',fontsize=7.3,fontweight='bold',color='white',zorder=3)
band(3,58,'TAREA SUPERVISADA · determinantes — competición base vs avanzado',BLUE); band(60,79,'NO SUPERVISADA · tipologías',GREEN); band(81,98,'SERIES · proyección',SLATE)
ax.add_patch(mpatches.FancyBboxPatch((7,82.6),44,2.5,boxstyle='round,pad=0.12',fc='#f5f6f8',ec='#c4cad2',lw=1.0,zorder=3,mutation_aspect=0.5))
_nt='mismo target (alquiler mediano)  ·  misma partición temporal'
ax.text(29,83.85,_nt,ha='center',va='center',fontsize=6.6,style='italic',color='#888',zorder=5)
YT=80.0
ridge=[('RIDGE — modelo base','head'),('Matriz 624×59 (sin fuga)','b'),('Estandarización (z-score)','b'),('α = 10 · CV temporal','b'),('R² 0,94  ·  MAE 16 €','metric')]
rf=[('RANDOM FOREST','head'),('Misma matriz 624×59','b'),('Sin escalado','b'),('','b'),('R² 0,61  ·  MAE 40 €','metric')]
gb=[('GRADIENT BOOSTING','head'),('Misma matriz 624×59','b'),('Sin escalado','b'),('Nº etapas por CV (lr 0,05)','b'),('R² 0,73  ·  MAE 31 €','metric')]
km=[('K-MEANS','head'),('Rasgos: nivel + tendencia','b'),('Estandarización','b'),('k = 3 (silueta + interpret.)','b'),('3 tipologías','out')]
ar=[('ARIMA','head'),('Serie del esfuerzo','b'),('ADF  →  d = 1','b'),('ARIMA(0,1,0) + deriva','b'),('37,1→36,9 % (>30 %)','out')]
bR=col(13,14.5,YT,ridge,BLUE,'#dbe5f2'); col(31,14.5,YT,rf,BLUE,'#dbe5f2'); col(49,14.5,YT,gb,BLUE,'#dbe5f2')
ax.text(31,57.3,'Árboles/prof. por OOB',ha='center',va='center',fontsize=6.7,color='#1a1a1a',zorder=4); cpill(31,55.2,'Figura 2',AMBF,AMBE,AMBT,fs=6.0)
col(70,17,YT,km,GREEN,'#e3f0e5'); col(89,17,YT,ar,SLATE,'#e6e2ef')
ax.text(22,YT-2.5,'vs',ha='center',fontsize=11,fontweight='bold',color=BLUE,zorder=5); ax.text(40,YT-2.5,'vs',ha='center',fontsize=11,fontweight='bold',color=BLUE,zorder=5)
for xx in (70,89): ax.annotate('',xy=(xx,bR-0.9),xytext=(xx,bR),arrowprops=dict(arrowstyle='-|>',color='#aaa',lw=1.0),zorder=2)
cpill(70,bR-2.1,'Figura 5',AMBF,AMBE,AMBT); cpill(89,bR-2.1,'Figura 6',AMBF,AMBE,AMBT)
ybus=bR-2.6
for xx in (13,31,49): ax.plot([xx,xx],[bR,ybus],color=GREEN,lw=1.4,zorder=2)
ax.plot([13,49],[ybus,ybus],color=GREEN,lw=1.4,zorder=2)
ygan=ybus-1.4; ax.annotate('',xy=(31,ygan),xytext=(31,ybus),arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=1.6),zorder=2)
rbox(31,52,ygan,5.2,'Comparación fuera de muestra · 7 ventanas 2018-2024     →     GANADOR: Ridge · R² 0,94',WIN,GREEN,True,8.0,'#1d5c3a',lw=1.7,asp=0.55); pill(59.0,ygan-2.6,'Tabla 2',AMBF,AMBE,AMBT)
yi=ygan-5.2-1.8; ax.annotate('',xy=(31,yi),xytext=(31,ygan-5.2),arrowprops=dict(arrowstyle='-|>',color='#888',lw=1.2),zorder=2)
rbox(31,52,yi,4.8,'Inferencia: efectos fijos LSDV + EE clusterizados + VIF','#eceaf4',SLATE,True,7.6,'#3d2f63',lw=1.4,asp=0.55); pill(59.0,yi-1.6,'Tabla 3',AMBF,AMBE,AMBT); pill(59.0,yi-4.0,'Figura 3',AMBF,AMBE,AMBT)
yv=yi-4.8-1.6; ax.annotate('',xy=(31,yv),xytext=(31,yi-4.8),arrowprops=dict(arrowstyle='-|>',color='#888',lw=1.1),zorder=2)
rbox(31,52,yv,5.2,'','white',BLUE,False,7.0,'#333',lw=1.2,asp=0.5)
ax.text(31,yv-1.5,'Diagnóstico Ridge: (a) predicho-vs-real · (b) residuos · (c) coeficientes',ha='center',va='center',fontsize=7.0,color='#333',zorder=5)
cpill(31,yv-3.8,'Figura 4',AMBF,AMBE,AMBT)
# Complementarios
yc=yv-5.2-2.0
ax.add_patch(mpatches.FancyBboxPatch((3,yc-2.8),95,2.8,boxstyle='round,pad=0.2',fc='#6b7280',ec='none',zorder=2)); ax.text(50,yc-1.4,'ANÁLISIS COMPLEMENTARIOS E INTERPRETACIÓN',ha='center',va='center',fontsize=8.6,fontweight='bold',color='white',zorder=3)
seqline(50,yc-4.3,[('t','robustez    ·    diagnóstico · comportamiento · traducción')],fs=7.0,tcol='#777')
itop=yc-5.6
cards=[(12,'Aportación incremental','+0,13 de R²','Tabla 4'),(30,'Residuos →\nmercados recalentados',None,'Tabla 5'),(48,'Gradiente por edad','72 % (18-25)\nvs  31 % (36-45)',None),(66,'Exposición territorial','97,9 %',None)]
for xc,lab,val,ref in cards:
    rbox(xc,16.5,itop,5.8,'','white','#9aa3ad',False,6.6,'#333',lw=1.1,asp=0.55)
    if ref and val:
        ax.text(xc,itop-1.4,lab,ha='center',va='center',fontsize=6.4,color='#333',zorder=5); ax.text(xc,itop-2.7,val,ha='center',va='center',fontsize=6.8,fontweight='bold',color='#1a1a1a',zorder=5); cpill(xc,itop-4.5,ref,AMBF,AMBE,AMBT,fs=5.8)
    elif ref:
        ax.text(xc,itop-1.95,lab,ha='center',va='center',fontsize=6.4,color='#333',zorder=5); cpill(xc,itop-4.35,ref,AMBF,AMBE,AMBT,fs=5.8)
    else:
        ax.text(xc,itop-1.7,lab,ha='center',va='center',fontsize=6.4,color='#333',zorder=5); ax.text(xc,itop-3.55,val,ha='center',va='center',fontsize=6.8,fontweight='bold',color='#1a1a1a',zorder=5)
rbox(86,21,itop,5.8,'→   ANÁLISIS\nDE NEGOCIO',WIN,GREEN,True,8.0,'#1d5c3a',lw=1.6,asp=0.55)
ax.annotate('',xy=(31,yc),xytext=(31,yv-5.2),arrowprops=dict(arrowstyle='-|>',color='#aaa',lw=1.1),zorder=2)
for xx in (70,89): ax.annotate('',xy=(xx,yc),xytext=(xx,bR-3.4),arrowprops=dict(arrowstyle='-|>',color='#bbb',lw=1.0),zorder=1)
# Leyenda + Herramientas
ax.add_patch(mpatches.FancyBboxPatch((3,3.4),46,6.2,boxstyle='round,pad=0.4',fc='#fafafa',ec='#bbb',lw=1,zorder=3))
ax.text(5.5,8.3,'Leyenda',fontsize=8,fontweight='bold',zorder=4)
ax.add_patch(plt.Rectangle((5.5,4.6),2.0,1.4,fc='white',ec=BLUE,zorder=4)); ax.text(8.6,5.3,'paso del modelo',fontsize=7.0,va='center',zorder=4)
ax.add_patch(plt.Rectangle((21,4.6),2.0,1.4,fc=MET,ec=BLUE,zorder=4)); ax.text(24.1,5.3,'métrica / R²',fontsize=7.0,va='center',zorder=4)
ax.add_patch(plt.Rectangle((34,4.6),2.0,1.4,fc=WIN,ec=GREEN,zorder=4)); ax.text(37.1,5.3,'ganador / salida',fontsize=7.0,va='center',zorder=4)
ax.add_patch(mpatches.FancyBboxPatch((51,3.4),47,6.2,boxstyle='round,pad=0.4',fc='#fafafa',ec='#bbb',lw=1,zorder=3))
ax.text(53.5,8.3,'Herramientas',fontsize=8,fontweight='bold',zorder=4)
ax.text(53.5,5.5,'Python · scikit-learn (Ridge, Random Forest, Gradient Boosting, K-Means)\nstatsmodels (OLS efectos fijos, ADF, ARIMA) · matplotlib / seaborn',fontsize=7.0,va='center',zorder=4)
plt.savefig(FIG_DIR/'Analisis_Fig01_flujo_metodologico.png',dpi=150,bbox_inches='tight'); display(fig); plt.close(fig)
print("OK -> figuras/Analisis_Fig01_flujo_metodologico.png")
