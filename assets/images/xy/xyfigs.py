import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def xPos(theta):
    return np.cos(theta)
def yPos(theta):
    return np.sin(theta)

def hamxy(grid):
    imShape = grid.shape
    energy = np.zeros(imShape)
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            #print(i,j)
            energy[i,j]= np.cos(col-grid[(i+1)%imShape[0],j]) + np.cos(col-grid[(i-1)%imShape[0],j])+np.cos(col-grid[i,(j+1)%imShape[0]])+np.cos(col-grid[i,(j+1)%imShape[0]])
    return -energy

def wNum(theta1,theta2):
    delA = theta1-theta2
    return delA-np.arcsin(np.sin(theta1-theta2))
def dCount(grid):
    imShape = grid.shape
    N = imShape[0]
    dgrid = np.zeros(imShape)
    wgrid = np.zeros(imShape)
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            wN = wNum(grid[i, (j-1)%N],col) +\
                 wNum(grid[ (i-1)%N, (j-1)%N], grid[i,(j-1)%N])+\
                 wNum(grid[ (i-1)%N, (j)%N],grid[ (i-1)%N, (j-1)%N])+\
                 wNum(col,grid[(i-1)%N, (j)%N])
            wgrid[i,j] = wN
            if (wN >= np.pi):
                dgrid[i,j] = 1
            elif (-wN >= np.pi):
                dgrid[i,j] = -1
    return (wgrid, dgrid)

#parser = argparse.ArgumentParser(description='Make some movies')
#parser.add_argument('fName',type=str,help='directory name for data')
#args = parser.parse_args()
##Sort fileNames by number

np.random.seed()
grid = np.random.rand(100).reshape([10,10])*2*np.pi-np.pi
simpleGrid = np.ones([10,10])*np.pi/4
fig,ax = plt.subplots()
ax.set_aspect(aspect='equal')
ax.axis('off')
X,Y = np.indices([10,10])
#ax.quiver(X,Y, xPos(imSeq[0]), yPos(imSeq[0]))
circ = []
for i,j in zip(X.ravel(),Y.ravel()):
    print(i,j)
    circ.append(plt.Circle((i,j),.1,zorder=2))
    ax.add_artist(circ[-1])

dCirc = []
dText = []
for i,j in zip(X[1:,:].ravel(),Y[:,1:].ravel()):
    print(i,j)
    dCirc.append(plt.Rectangle((i-1,j-1),1,1,alpha=.1,edgecolor=None,facecolor='white',zorder=0))
    ax.add_artist(dCirc[-1])
    dText.append(plt.Text(x=i-.5,y=j-.5, text='',fontsize=12,va='center',ha='center',zorder=1))
    ax.add_artist(dText[-1])
dCirc = np.array(dCirc)
dText = np.array(dText)
#f1 = imSeq[0]
#U = xPos(f1)
#JV = yPos(f1)
#gg = hamxy(f1)
#dL = dCount(f1)
#pD = np.where(dL==1)[0]
#mD = np.where(dL==-1)[0]
#[c.set_facecolor('blue') for c in dCirc[mD]]
#[c.set_facecolor('red') for c in dCirc[pD]]
    
#Q=ax.quiver(X,Y, U,V,gg,scale=15,cmap='copper')
#ax.axis('off')
    
ax.set_title('grid')
ax.set_xlim([-1,11])
ax.set_ylim([-1,11])



fig.tight_layout
fig.savefig('basic-grid.png')
#plt.close('all')

#now, add spins
f1 = simpleGrid
U = xPos(f1)
V = yPos(f1)
gg = hamxy(f1)
wl, dL = dCount(f1)
pD = np.where(dL[1:,1:]==1)[0]
mD = np.where(dL[1:,1:]==-1)[0]
#[c.set_facecolor('blue') for c in dCirc[mD]]
#[c.set_facecolor('red') for c in dCirc[pD]]
   
Q=ax.quiver(X,Y, U,V,gg,scale=20,zorder=3)#),cmap='copper')
fig.savefig('grid-spin1.png')

# now randomize spins
f1 = grid
U = xPos(f1)
V = yPos(f1)
gg = hamxy(f1)
wl,dL = dCount(f1)
pD = np.where(dL==1)[0]
mD = np.where(dL==-1)[0]
#[c.set_facecolor('blue') for c in dCirc[mD]]
#[c.set_facecolor('red') for c in dCirc[pD]]
   
Q.set_UVC(U,V)

#now, plot hamiltonian

fig2,ax2 = plt.subplots()
hamIm=ax2.imshow(gg,cmap = 'copper')
ax2.axis('off')
plt.colorbar(hamIm,ax=ax2)
ax2.set_title('hamiltonian')
fig2.savefig('random-hamil.png')

plt.close(fig2)
#now, color the spins by the hamilotonian

#Q.set_UVC(U,V,gg))
Q.remove()
Q=ax.quiver(X,Y, U,V,gg,scale=20,cmap='copper',zorder=3)
fig.savefig('random-colored-spins.png')

#now, add in defect tracking

# now randomize spins
f1 = grid
U = xPos(f1)
V = yPos(f1)
gg = hamxy(f1)
wl,dL = dCount(f1)
pD = np.where(dL[1:,1:].ravel()==1)[0]
mD = np.where(dL[1:,1:].ravel()==-1)[0]
Q.set_UVC(U,V,gg)

pos =[X.ravel(),Y.ravel()]
[c.set_facecolor('blue') for c in dCirc[mD]]
[c.set_facecolor('red') for c in dCirc[pD]]
[c.set_text('+') for c in dText[pD]]
[c.set_text('-') for c in dText[mD]]
ax.set_title('grid with defects')

fig.savefig('labeled-defects.png')

plt.close('all')


def vortex(px, py, mx, my, grid):
    x, y = np.indices(grid.shape)
    return np.mod(grid+np.arctan2((x-px), (y-py))-np.arctan2((x-mx), (y-my)), 2*np.pi)-np.pi


fig3, ax3 = plt.subplots()
ax3.set_aspect(aspect='equal')
ax3.axis('off')
testGrid = np.zeros([20, 20])
testGrid = vortex(5-.5, 5-.5, 12-.5, 12-.5,testGrid)
f1 = testGrid
X, Y = np.indices(testGrid.shape)
U = xPos(f1)
V = yPos(f1)
gg = hamxy(f1)
wl, dL = dCount(f1)
pD = np.where(dL.ravel() == 1)[0]
mD = np.where(dL.ravel() == -1)[0]
ax3.quiver(X, Y, U, V)


circ = {}
for i,j in zip(X.ravel(),Y.ravel()):
    print(i,j)
    circ[(i,j)]=(plt.Circle((i,j),.1,zorder=2))
    ax3.add_artist(circ[(i,j)])

dCirc = {}
dText = {}
for i, j in zip(X[1:, :].ravel(), Y[:, 1:].ravel()):
    print(i, j)
    dCirc[(i,j)]=(plt.Rectangle(
        (i-1, j-1), 1, 1, alpha=.1, edgecolor='k', facecolor='white', zorder=0) )
    ax3.add_artist(dCirc[(i,j)])
    dText[(i,j)]=(plt.Text(x=i-.5, y=j-.5, text='',fontsize=12, va='center', ha='center', zorder=1))
    ax3.add_artist(dText[(i,j)])
#dCirc = np.array(dCirc)
#dText = np.array(dText)

pos = [X.ravel(), Y.ravel()]
xpDefect = X.ravel()[pD]
ypDefect = Y.ravel()[pD]
xmDefect = X.ravel()[mD]
ymDefect = Y.ravel()[mD]

pDefect = np.vstack([xpDefect,ypDefect]).T
mDefect = np.vstack([xmDefect,ymDefect]).T
[dCirc[tuple(loc)].set_facecolor('blue') for loc in mDefect]
[dCirc[tuple(loc)].set_facecolor('red') for loc in pDefect]


[dText[tuple(loc)].set_text('+') for loc in pDefect]
[dText[tuple(loc)].set_text('-') for loc in mDefect]
ax.set_title('grid with defects')
#ax3.set_xlim([-1, 11])
#ax3.set_ylim([-1, 11])
#plt.close('all')

#make single vortex at center of grid
plt.savefig('2defects.png')


fig4, ax4 = plt.subplots()
ax4.set_aspect(aspect='equal')
testGrid = np.zeros([20, 20])
pList = []
mList = []
np.random.seed(403)
for ii in np.arange(10):
    pList.append([np.random.randint(17)+1.5,np.random.randint(17)+1.5])
    mList.append([np.random.randint(17)+1.5,np.random.randint(17)+1.5])
    testGrid = vortex(*pList[-1], *mList[-1], testGrid)
f1 = testGrid
X, Y = np.indices(testGrid.shape)
U = xPos(f1)
V = yPos(f1)
gg = hamxy(f1)
wl,dL = dCount(f1)
pD = np.where(dL.ravel() == 1)[0]
mD = np.where(dL.ravel() == -1)[0]
ax4.quiver(X,Y, U, V)

circ = {}
for i,j in zip(X.ravel(),Y.ravel()):
    print(i,j)
    circ[(i,j)]=(plt.Circle((i,j),.1,zorder=2))
    ax4.add_artist(circ[(i,j)])

dCirc = {}
dText = {}
for i, j in zip(X[1:, :].ravel(), Y[:, 1:].ravel()):
    print(i, j)
    dCirc[(i,j)]=(plt.Rectangle(
        (i-1, j-1), 1, 1, alpha=.1, edgecolor='k', facecolor='white', zorder=0) )
    ax4.add_artist(dCirc[(i,j)])
    dText[(i,j)]=(plt.Text(x=i-.5, y=j-.5, text='',fontsize=12, va='center', ha='center', zorder=1))
    ax4.add_artist(dText[(i,j)])
#dCirc = np.array(dCirc)
#dText = np.array(dText)

pos = [X.ravel(), Y.ravel()]
xpDefect = X.ravel()[pD]
ypDefect = Y.ravel()[pD]
xmDefect = X.ravel()[mD]
ymDefect = Y.ravel()[mD]

pDefect = np.vstack([xpDefect,ypDefect]).T
mDefect = np.vstack([xmDefect,ymDefect]).T
[dCirc[tuple(loc)].set_facecolor('blue') for loc in pDefect]
[dCirc[tuple(loc)].set_facecolor('red') for loc in mDefect]
#[c.set_facecolor('red') for c in dCirc[pD]]
for i in np.arange(10):
    ax4.add_artist(plt.Text(x=pList[i][0],y=pList[i][1], text="+", va='center',ha='center'))
    ax4.add_artist(plt.Text(x=mList[i][0],y=mList[i][1], text="-", va='center',ha='center'))
#[c.set_text('+') for c in dText[pD]]
#[c.set_text('-') for c in dText[mD]]
ax4.set_title('grid with defects')
#ax3.set_xlim([-1, 11])
#ax3.set_ylim([-1, 11])
#plt.close('all')
plt.savefig('test40.png')
