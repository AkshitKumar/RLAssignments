OUT = herd_management_0.9
BINDIR = ../bin
OBJDIR = ../obj
OBJS = $(OBJDIR)/main.o $(OBJDIR)/action.o $(OBJDIR)/state.o $(OBJDIR)/afterstate.o $(OBJDIR)/pre_compute.o $(OBJDIR)/aux_methods.o

CC = g++
DEBUG = -g
CFLAGS = -Wall -c $(DEBUG)
LFLAGS = -Wall $(DEBUG)


$(BINDIR)/$(OUT): $(OBJS)
	$(CC) $(LFLAGS) $(OBJS) -o $(BINDIR)/$(OUT)
	chmod 777 $(BINDIR)/$(OUT)

$(OBJDIR)/main.o: main.cpp header.h parameter.h pre_compute.h state.h afterstate.h action.h
	$(CC) $(CFLAGS) main.cpp -o $(OBJDIR)/main.o
	chmod 777 $(OBJDIR)/main.o

$(OBJDIR)/pre_compute.o: pre_compute.cpp pre_compute.h header.h parameter.h state.h afterstate.h action.h aux_methods.h
	$(CC) $(CFLAGS) pre_compute.cpp -o $(OBJDIR)/pre_compute.o
	chmod 777 $(OBJDIR)/pre_compute.o

$(OBJDIR)/state.o: state.cpp state.h parameter.h
	$(CC) $(CFLAGS) state.cpp -o $(OBJDIR)/state.o
	chmod 777 $(OBJDIR)/state.o

$(OBJDIR)/afterstate.o: afterstate.cpp afterstate.h state.h parameter.h
	$(CC) $(CFLAGS) afterstate.cpp -o $(OBJDIR)/afterstate.o
	chmod 777 $(OBJDIR)/afterstate.o

$(OBJDIR)/action.o: action.cpp action.h header.h
	$(CC) $(CFLAGS) action.cpp -o $(OBJDIR)/action.o
	chmod 777 $(OBJDIR)/action.o

$(OBJDIR)/aux_methods.o: aux_methods.cpp aux_methods.h header.h parameter.h
	$(CC) $(CFLAGS) aux_methods.cpp -o $(OBJDIR)/aux_methods.o
	chmod 777 $(OBJDIR)/aux_methods.o


clean:
	rm -f $(BINDIR)/$(OUT) $(OBJS)
