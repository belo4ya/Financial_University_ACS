package com.java.Shapes;

public class Cylinder extends SolidOfRevolution {
    protected double height;

    public Cylinder(double radius, double height) {
        super(radius);
        this.height = height;
    }

    public double getHeight() {
        return height;
    }
}
