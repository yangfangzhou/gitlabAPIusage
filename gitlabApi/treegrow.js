var drawtree = function (ctx,startx,starty,length,angle,depth,branchWidth){
        var rand=Math.random,
        n_length,n_angle,n_depth,maxbranch=4,
        endx,endy,maxangle=2 * Math.PI / 4;
        var subbranch;
        ctx.beginPath();
        ctx.moveTo(startx,starty);
        endx=startx + length * Math.cos(angle);
        endy=starty + length * Math.sin(angle);
        ctx.lineCap='round';
        ctx.lineWidth=branchWidth;
        /*
        for (var i = 0;i < endx ;i++){
            ys = endy * i *0.5;
        ctx.lineTo(endx,endy < ys ? ys : ys + 300 );
        }
        */
        ctx.lineTo(endx,endy);
        if(depth<=2 ){
            //树的枝干
            ctx.strokeStyle= 'rgb(0,0,0)';
        }
        else{
            //树的叶子
//            ctx.strokeStyle= 'rgb(0,' + (((rand() * 64) +0) >>0) + ',50,25)';
            ctx.strokeStyle= 'rgb(0,0,0)';
        }
        ctx.stroke();
        

        
        n_depth = depth - 1;
        
        
        //判断树是否结束
        if(!n_depth){
            return;
        }
        subbranch= (rand() * (maxbranch-1)) + 1;
        branchWidth *=0.5; 
        for(var i=0;i<subbranch;i++){
            n_angle = angle +rand() * maxangle -maxangle *0.5;
            n_length = length * (0.5 + rand() *0.5);
            setTimeout(function (){
                drawtree(ctx,endx,endy,n_length,n_angle,n_depth,branchWidth);
                return;
            },100)
        }
    }



