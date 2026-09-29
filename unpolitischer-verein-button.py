from pythonscad import *
import pincutout
import os

fn=64

unpolitischer_verein_parts = osimport("unpolitischer_verein.svg", split_by_color=True)

unpolitischer_verein_position = union(
    list(unpolitischer_verein_parts.values())
).position
unpolitischer_verein_size = union(list(unpolitischer_verein_parts.values())).size
unpolitischer_verein_parts = {
    name: obj.translate([i * -1 for i in unpolitischer_verein_position]).linear_extrude(
        2
    )
    for name, obj in unpolitischer_verein_parts.items()
}

cutout_object = pincutout.PinCutout(
    length=25.5,
    width=5.1,
    depth=0.4,
    knob_diameter=2,
    knob_gap=6,
    epsilon=0.001,
    fn=256,
).render()

cutout_object = cutout_object.translate(
    [(unpolitischer_verein_size[0] - cutout_object.size[0]) / 2, 28, 0]
)


mte = MultiToolExporter()
mte.extend(unpolitischer_verein_parts.items())
mte.append(("cutout", cutout_object, False))


mte.export(
    single_file=os.path.join(
        os.path.dirname(modelpath()), "out", "unpolitischer-verein-pin.3mf"
    ),
    mkdir=True
)
mte.show()
