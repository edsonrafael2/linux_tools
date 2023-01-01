#!/bin/bash

run(){

sudo dd if=/dev/sdb of=/dev/sdc bs=4096 conv=noerror,sync

}

run

