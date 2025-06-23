# Soccer Ball Kicker Project

The aim of this project is to create an assistive device that can be used by individuals with limited mobility to kick a soccer ball.

## Phase 1: Code and Proof-of-Concept

[Prototype Operating](./Photos/prototype1.gif)

The goal of this phase is to create an "abstract" demo unit to show off the code.

This phase will be considered complete when:

- A motor should react to the push of a button
- Upon reacting, the motor should move forward in one direction and then return the same number of steps in the opposite direction.
- There should be a "cool-down" period of 1-2 seconds to prevent double firing
- A 3D printed shell for the electronics has been drafted.

**Phase Timeline**

| Date    | Description                            |
| ------- | -------------------------------------- |
| 6/23/25 | Initialized GitHub repository          |
| 6/23/25 | Drafted `kicker.py` with place-holders |
| 6/23/25 | Prototype with RPi 4                   |

### Code and Hardware Considerations

**Materials Used in this Phase**

| Material               | Quantity | Notes                           |
| ---------------------- | -------- | ------------------------------- |
| 5-24V Battery Bank     | 1        | Power RPi and motor separately  |
| Raspberry Pi Zero 2W   | 1        | Desbian Lite Installation       |
| Breadboard             | 1        |                                 |
| 5V Stepper Motor       | 1        |                                 |
| Motor Controller Board | 1        |                                 |
| Button                 | 2        | Soft kick and hard kick buttons |
| DuPont Cables          | Many     |                                 |

I selected a Raspberry Pi Zero 2W as my SBC for the project, although I am sure an Arduino or other SBC would work fine. Running Linux Raspbian Lite.

The code for this project is written in Python to be able to utilize the `RPi` library. All code can be found in the files at the top of the repo.

The initial code build uses a stepper motor for moving the leg. I would like to also explore the use of a servo motor, as I think it will be a better fit for a fast-moving actuation.

## Phase 2: Power and Torque

In this phase, I will:

- Determine proper motor type and power requirements
- Determine gearing requirements for the amount of torque I will need for kicking a soccer ball

## Phase 3: Lab Testing

In this phase, the unit will be tested a troubleshot within a controlled environment. The safety of the device must be satisfactory before moving to field testing.

This phase will be considered complete when:

- The unit kicks a ball with 95% reliability or greater.
- The safety considerations of the unit have been fully assessed.

## Phase 4: Field Testing

This phase will involve testing the functionality of the device with real participant subjects.

This phase will be considered complete when:

- The device has been tested in the field by no less than three (3)
- Feedback from participants has been collected

## Phase 5: Interative Refinement

TBD
