import bi_unars
cxt = bi_unars.generate_context(3, bi_unars.attributes)
#basis = cxt.attribute_implications
back = bi_unars.generate_background_implications(bi_unars.attributes)
relative = cxt.get_attribute_implications(confirmed=back)
symm_relative = cxt.get_attribute_implications(confirmed=back, cond=bi_unars.is_orbit_maximal)

e = bi_unars.expert
e.explore(bi_unars.exploration)
