class Fork {
    public final int id;

    private Philosopher owner;

    Fork(int id) {
        this.id = id;
    }

    public int getOwner() {
        if (this.owner != null) {
            return owner.id;
        }
        return -1;
    }

    public synchronized boolean grab(Philosopher owner) {
        if (this.owner == null) {
            this.owner = owner;
            String msg = "Fork " + Integer.toString(this.id) + " picked up by philosopher " + Integer.toString(owner.id);
            System.out.println(msg);
            return true;
        } else if (Math.random() < 0.75) {
            this.release(this.owner);
            this.grab(owner);
            return true;
        }
        return false;
    }

    public synchronized boolean release(Philosopher owner) {
        if (this.owner == owner) {
            this.owner = null;
            String msg = "Fork " + Integer.toString(this.id) + " put down by philosopher " + Integer.toString(owner.id);
            System.out.println(msg);
            return true;
        }
        return false;
    }
}

class Philosopher extends Thread {
    public final int id;
    public final Fork left;
    public final Fork right;
    private int count;
    Philosopher(int id, int count, Fork left, Fork right) {
        this.id = id;
        this.count = count;
        this.left = left;
        this.right = right;
    }

    public void run() {
        System.out.println("Philosopher " + Integer.toString(this.id) + " has sat down at the table.");
        while (count > 0) {
            this.grabRight();
            this.grabLeft();
            if (this.eatSpaghetti()) {
                this.releaseLeft();
                this.releaseRight();
            }
        }
        System.out.println("Philosopher " + Integer.toString(this.id) + " has finished eating.");
    }

    private boolean grabLeft() {
        return this.left.grab(this);
    }

    private boolean releaseLeft() {
        return this.left.release(this);
    }

    private boolean grabRight() {
        return this.right.grab(this);
    }

    private boolean releaseRight() {
        return this.right.release(this);
    }

    private boolean eatSpaghetti() {
        if (this.left.getOwner() == this.id && this.right.getOwner() == this.id) {
            String msg = "Philosopher " + Integer.toString(this.id) + " eating spaghetti. " + Integer.toString(this.count) + " left.";
            System.out.println(msg);
            this.count -= 1;
            return true;
        }
        return false;
    }
}

class Program {
    public static void main(String[] args) {
        int count = 5;
        Fork[] forks = new Fork[count];
        Philosopher[] philosophers = new Philosopher[count];
        for (int i = 0; i < count; i += 1) {
            forks[i] = new Fork(i + 1);
        }
        for (int i = 0; i < count; i += 1) {
            philosophers[i] = new Philosopher(i + 1, 10, forks[i], forks[(i + 1) % count]);
            philosophers[i].start();
        }
        boolean finished = false;
        while(!finished) {
            for (int i = 0; i < count; i += 1) {
                if (philosophers[i].isAlive()) {
                    Thread.yield();
                } else {
                    finished = true;
                }
            }
        }
    }
}
