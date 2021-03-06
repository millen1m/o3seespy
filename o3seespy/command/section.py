from o3seespy.base_model import OpenSeesObject


class SectionBase(OpenSeesObject):
    op_base_type = "section"


class Elastic2D(SectionBase):
    """
    The Elastic2D Section Class
    
    
    """
    op_type = 'Elastic'

    def __init__(self, osi, e_mod, area, iz, g_mod: float=None, alpha_y: float=None):
        """
        Initial method for Elastic2D

        Parameters
        ----------
        e_mod: float
            Young's modulus
        area: float
            Cross-sectional area of section
        iz: float
            Second moment of area about the local z-axis
        g_mod: float (default=True)
            Shear modulus (optional for 2d analysis, required for 3d analysis)
        alpha_y: float (default=True)
            Shear shape factor along the local y-axis (optional)
        """
        self.e_mod = float(e_mod)
        self.area = float(area)
        self.iz = float(iz)
        if g_mod is None:
            self.g_mod = None
        else:
            self.g_mod = float(g_mod)
        if alpha_y is None:
            self.alpha_y = None
        else:
            self.alpha_y = float(alpha_y)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.e_mod, self.area, self.iz]
        special_pms = ['g_mod', 'alpha_y']
        packets = [False, False]
        for i, pm in enumerate(special_pms):
            if getattr(self, pm) is not None:
                if packets[i]:
                    self._parameters += [*getattr(self, pm)]
                else:
                    self._parameters += [getattr(self, pm)]
            else:
                break
        self.to_process(osi)


class Elastic3D(SectionBase):
    """
    The Elastic3D Section Class
    
    This command allows the user to construct an ElasticSection. The inclusion of shear deformations is optional. The
    dofs for 2D elastic section are ``[P, Mz]``,for 3D are ``[P,Mz,My,T]``.
    """
    op_type = 'Elastic'

    def __init__(self, osi, e_mod, area, iz, iy, g_mod, jxx, alpha_y: float=None, alpha_z: float=None):
        """
        Initial method for Elastic3D

        Parameters
        ----------
        e_mod: float
            Young's modulus
        area: float
            Cross-sectional area of section
        iz: float
            Second moment of area about the local z-axis
        iy: float
            Second moment of area about the local y-axis (required for 3d analysis)
        g_mod: float
            Shear modulus (optional for 2d analysis, required for 3d analysis)
        jxx: float
            Torsional moment of inertia of section (required for 3d analysis)
        alpha_y: float (default=True)
            Shear shape factor along the local y-axis (optional)
        alpha_z: float (default=True)
            Shear shape factor along the local z-axis (optional)
        """
        self.e_mod = float(e_mod)
        self.area = float(area)
        self.iz = float(iz)
        self.iy = float(iy)
        self.g_mod = float(g_mod)
        self.jxx = float(jxx)
        if alpha_y is None:
            self.alpha_y = None
        else:
            self.alpha_y = float(alpha_y)
        if alpha_z is None:
            self.alpha_z = None
        else:
            self.alpha_z = float(alpha_z)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.e_mod, self.area, self.iz, self.iy, self.g_mod, self.jxx]
        special_pms = ['alpha_y', 'alpha_z']
        packets = [False, False]
        for i, pm in enumerate(special_pms):
            if getattr(self, pm) is not None:
                if packets[i]:
                    self._parameters += [*getattr(self, pm)]
                else:
                    self._parameters += [getattr(self, pm)]
            else:
                break
        self.to_process(osi)


class Fiber(SectionBase):
    """
    The Fiber Section Class

    This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers,
    with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P,
    Mz]``,for 3D are ``[P,Mz,My,T]``.
    """
    op_type = 'Fiber'

    def __init__(self, osi, gj: float = None, torsion_mat=None):
        """
        Initial method for Fiber

        Parameters
        ----------
        gj: float
            Linear-elastic torsional stiffness assigned to the section
        torsion_mat: obj
            Uniaxialmaterial tag assigned to the section for torsional response (can be nonlinear)
        """
        if gj is None:
            self.gj = None
        else:
            self.gj = float(gj)
        self.torsion_mat = torsion_mat
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag]
        if getattr(self, 'gj') is not None:
            self._parameters += ['-GJ', self.gj]
        if getattr(self, 'torsion_mat') is not None:
            self._parameters += ['-torsion', self.torsion_mat.tag]
        self.to_process(osi)


class Fiber(SectionBase):
    """
    The Fiber Section Class

    This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers,
    with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P,
    Mz]``,for 3D are ``[P,Mz,My,T]``.
    """
    op_type = 'Fiber'

    def __init__(self, osi, gj: float = None, torsion_mat=None):
        """
        Initial method for Fiber

        Parameters
        ----------
        gj: float
            Linear-elastic torsional stiffness assigned to the section
        torsion_mat: obj
            Uniaxialmaterial tag assigned to the section for torsional response (can be nonlinear)
        """
        if gj is None:
            self.gj = None
        else:
            self.gj = float(gj)
        self.torsion_mat = torsion_mat
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag]
        if getattr(self, 'gj') is not None:
            self._parameters += ['-GJ', self.gj]
        if getattr(self, 'torsion_mat') is not None:
            self._parameters += ['-torsion', self.torsion_mat.tag]
        self.to_process(osi)


class Fiber(SectionBase):
    """
    The Fiber Section Class

    This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers,
    with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P,
    Mz]``,for 3D are ``[P,Mz,My,T]``.
    """
    op_type = 'Fiber'

    def __init__(self, osi, gj: float = None, torsion_mat=None):
        """
        Initial method for Fiber

        Parameters
        ----------
        gj: float
            Linear-elastic torsional stiffness assigned to the section
        torsion_mat: obj
            Uniaxialmaterial tag assigned to the section for torsional response (can be nonlinear)
        """
        if gj is None:
            self.gj = None
        else:
            self.gj = float(gj)
        self.torsion_mat = torsion_mat
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag]
        if getattr(self, 'gj') is not None:
            self._parameters += ['-GJ', self.gj]
        if getattr(self, 'torsion_mat') is not None:
            self._parameters += ['-torsion', self.torsion_mat.tag]
        self.to_process(osi)



class FiberThermal(SectionBase):
    """
    The FiberThermal Section Class
    
    This command create a FiberSectionThermal object.The dofs for 2D section are ``[P, Mz]``,for 3D are ``[P,Mz,My]``...
    note::#. The commands below should be called after the section command to generate all the fibers in the section.#. The
    patch and layer commands can be used to generate multiple fibers in a single command... toctree:::maxdepth: 2:caption:
    Commands to generate all fibersfiberpatchlayer
    """
    op_type = 'FiberThermal'

    def __init__(self, osi, gj=None):
        """
        Initial method for FiberThermal

        Parameters
        ----------
        gj: None
            
        """
        self.gj = gj
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag]
        if getattr(self, 'gj') is not None:
            self._parameters += ['-GJ', self.gj]
        self.to_process(osi)


class NDFiber(SectionBase):
    """
    The NDFiber Section Class
    
    This commnand allows the user to construct an NDFiberSection object. Each NDFiberSection object is composed of
    NDFibers, with each fiber containing an NDMaterial, an area and a location (y,z). The NDFiberSection works for 2D
    and 3D frame elements and it queries the NDMaterial of each fiber for its axial and shear stresses. In 2D,
    stress components 11 and 12 are obtained from each fiber in order to provide stress resultants for axial
    force, bending moment, and shear ``[P, Mz, Vy]``. Stress components 11, 12, and 13 lead to all six
    stress resultants in 3D ``[P, Mz, Vy, My, Vz, T]``.The NDFiberSection works with any NDMaterial
    via wrapper classes that perform static condensation of the stress vector down to the 11, 12,
    and 13 components, or via concrete NDMaterial subclasses that implement the appropriate fiber stress conditions.
    """
    op_type = 'NDFiber'

    def __init__(self, osi):
        """
        Initial method for NDFiber

        Parameters
        ----------
        """
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag]
        self.to_process(osi)


class WFSection2D(SectionBase):
    """
    The WFSection2D Section Class
    
    This command allows the user to construct a WFSection2d object, which is an encapsulated fiber representation of a
    wide flange steel section appropriate for plane frame analysis.
    """
    op_type = 'WFSection2d'

    def __init__(self, osi, mat, d, tw, bf, tf, nfw, nff):
        """
        Initial method for WFSection2D

        Parameters
        ----------
        mat: obj
            Tag of uniaxialmaterial assigned to each fiber
        d: float
            Section depth
        tw: float
            Web thickness
        bf: float
            Flange width
        tf: float
            Flange thickness
        nfw: float
            Number of fibers in the web
        nff: float
            Number of fibers in each flange
        """
        self.mat = mat
        self.d = float(d)
        self.tw = float(tw)
        self.bf = float(bf)
        self.tf = float(tf)
        self.nfw = float(nfw)
        self.nff = float(nff)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.mat.tag, self.d, self.tw, self.bf, self.tf, self.nfw, self.nff]
        self.to_process(osi)


class RCSection2D(SectionBase):
    """
    The RCSection2D Section Class
    
    This command allows the user to construct an RCSection2d object, which is an encapsulated fiber representation of a
    rectangular reinforced concrete section with core and confined regions of concrete and single top and bottom layers of
    reinforcement appropriate for plane frame analysis.
    """
    op_type = 'RCSection2d'

    def __init__(self, osi, core_mat, cover_mat, steel_mat, d, b, cover_depth, atop, abot, aside, nfcore, nfcover, nfs):
        """
        Initial method for RCSection2D

        Parameters
        ----------
        core_mat: obj
            Tag of uniaxialmaterial assigned to each fiber in the core region
        cover_mat: obj
            Tag of uniaxialmaterial assigned to each fiber in the cover region
        steel_mat: obj
            Tag of uniaxialmaterial assigned to each reinforcing bar
        d: float
            Section depth
        b: float
            Section width
        cover_depth: float
            Cover depth (assumed uniform around perimeter)
        atop: float
            Area of reinforcing bars in top layer
        abot: float
            Area of reinforcing bars in bottom layer
        aside: float
            Area of reinforcing bars on intermediate layers
        nfcore: float
            Number of fibers through the core depth
        nfcover: float
            Number of fibers through the cover depth
        nfs: float
            Number of bars on the top and bottom rows of reinforcement (nfs-2 bars will be placed on the side rows)
        """
        self.core_mat = core_mat
        self.cover_mat = cover_mat
        self.steel_mat = steel_mat
        self.d = float(d)
        self.b = float(b)
        self.cover_depth = float(cover_depth)
        self.atop = float(atop)
        self.abot = float(abot)
        self.aside = float(aside)
        self.nfcore = float(nfcore)
        self.nfcover = float(nfcover)
        self.nfs = float(nfs)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.core_mat.tag, self.cover_mat.tag, self.steel_mat.tag, self.d, self.b, self.cover_depth, self.atop, self.abot, self.aside, self.nfcore, self.nfcover, self.nfs]
        self.to_process(osi)


class RCCircularSection(SectionBase):
    """
    The RCCircularSection Section Class
    
    This command allows the user to construct an RCCircularSection object, which is an encapsulated fiber representation
    of a circular reinforced concrete section with core and confined regions of concrete.
    """
    op_type = 'RCCircularSection'

    def __init__(self, osi, core_mat, cover_mat, steel_mat, d, cover_depth, a_s, nrings_core, nrings_cover, newedges, nsteel, gj: float=None):
        """
        Initial method for RCCircularSection

        Parameters
        ----------
        core_mat: obj
            Tag of uniaxialmaterial assigned to each fiber in the core region
        cover_mat: obj
            Tag of uniaxialmaterial assigned to each fiber in the cover region
        steel_mat: obj
            Tag of uniaxialmaterial assigned to each reinforcing bar
        d: float
            Section radius
        cover_depth: float
            Cover depth (assumed uniform around perimeter)
        a_s: float
            Area of reinforcing bars 
        nrings_core: int
            Number of fibers through the core depth
        nrings_cover: int
            Number of fibers through the cover depth
        newedges: int
            Number of fibers through the edges
        nsteel: int
            Number of fibers through the steels
        gj: float
            Gj stiffness
        """
        self.core_mat = core_mat
        self.cover_mat = cover_mat
        self.steel_mat = steel_mat
        self.d = float(d)
        self.cover_depth = float(cover_depth)
        self.a_s = float(a_s)
        self.nrings_core = int(nrings_core)
        self.nrings_cover = int(nrings_cover)
        self.newedges = int(newedges)
        self.nsteel = int(nsteel)
        if gj is None:
            self.gj = None
        else:
            self.gj = float(gj)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.core_mat.tag, self.cover_mat.tag, self.steel_mat.tag, self.d, self.cover_depth, self.a_s, self.nrings_core, self.nrings_cover, self.newedges, self.nsteel]
        if getattr(self, 'gj') is not None:
            self._parameters += ['-GJ', self.gj]
        self.to_process(osi)


class Parallel(SectionBase):
    """
    The Parallel Section Class
    
    Connect sections in parallel.
    """
    op_type = 'Parallel'

    def __init__(self, osi, secs):
        """
        Initial method for Parallel

        Parameters
        ----------
        secs: list
            Tags of of predefined sections.
        """
        self.secs = [x.tag for x in secs]
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, *self.secs]
        self.to_process(osi)


class Aggregator(SectionBase):
    """
    The Aggregator Section Class

    This command is used to construct a SectionAggregator object which aggregates groups previously-defined
    UniaxialMaterial objects into a single section force-deformation model. Each UniaxialMaterial object
    represents the section force-deformation response for a particular section degree-of-freedom (dof).
    There is no interaction between responses in different dof directions. The aggregation can include
    one previously defined section.
    """
    op_type = 'Aggregator'

    def __init__(self, osi, mats, section=None):
        """
        Initial method for Aggregator

        Parameters
        ----------
        mats: list
            List of mat objs and dofs of previously-defined uniaxialmaterial objects, ``mats =
            [[mattag1,dof1],[mattag2,dof2],...]`` the force-deformation quantity to be modeled by this
            section object. one of the following section dof may be used: * ``'p'`` axial
            force-deformation * ``'mz'`` moment-curvature about section local z-axis *
            ``'vy'`` shear force-deformation along section local y-axis * ``'my'``
            moment-curvature about section local y-axis * ``'vz'`` shear
            force-deformation along section local z-axis * ``'t'`` torsion force-deformation
        section: obj
            Tag of previously-defined section object to which the uniaxialmaterial objects are aggregated as additional
            force-deformation relationships (optional)
        """
        self.mats = []
        for i, mat in enumerate(mats):
            self.mats.append(mats[i][0].tag)
            self.mats.append(mats[i][1])
        self.section = section
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, *self.mats]
        if getattr(self, 'section') is not None:
            self._parameters += ['-section', self.section.tag]
        self.to_process(osi)



class Uniaxial(SectionBase):
    """
    The Uniaxial Section Class
    
    This command is used to construct a UniaxialSection object which uses a previously-defined UniaxialMaterial object
    to represent a single section force-deformation response quantity.
    """
    op_type = 'Uniaxial'

    def __init__(self, osi, mat, quantity):
        """
        Initial method for Uniaxial

        Parameters
        ----------
        mat: obj
            Tag of uniaxial material
        quantity: str
            The force-deformation quantity to be modeled by this section object. one of the following section dof may be
            used: * ``'p'`` axial force-deformation * ``'mz'`` moment-curvature about section local z-axis * ``'vy'`` shear
            force-deformation along section local y-axis * ``'my'`` moment-curvature about section local y-axis * ``'vz'``
            shear force-deformation along section local z-axis * ``'t'`` torsion force-deformation
        """
        self.mat = mat
        self.quantity = quantity
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.mat.tag, self.quantity]
        self.to_process(osi)


class ElasticMembranePlateSection(SectionBase):
    """
    The ElasticMembranePlateSection Section Class
    
    This command allows the user to construct an ElasticMembranePlateSection object, which is an isotropic section
    appropriate for plate and shell analysis.
    """
    op_type = 'ElasticMembranePlateSection'

    def __init__(self, osi, e_mod, nu, h, rho):
        """
        Initial method for ElasticMembranePlateSection

        Parameters
        ----------
        e_mod: float
            Young's modulus
        nu: float
            Poisson's ratio
        h: float
            Depth of section
        rho: float
            Mass density
        """
        self.e_mod = float(e_mod)
        self.nu = float(nu)
        self.h = float(h)
        self.rho = float(rho)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.e_mod, self.nu, self.h, self.rho]
        self.to_process(osi)


class PlateFiber(SectionBase):
    """
    The PlateFiber Section Class
    
    This command allows the user to construct a MembranePlateFiberSection object, which is a section that numerically
    integrates through the plate thickness with "fibers" and is appropriate for plate and shell analysis.
    """
    op_type = 'PlateFiber'

    def __init__(self, osi, mat, h):
        """
        Initial method for PlateFiber

        Parameters
        ----------
        mat: obj
            Ndmaterial tag to be assigned to each fiber
        h: float
            Plate thickness
        """
        self.mat = mat
        self.h = float(h)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.mat.tag, self.h]
        self.to_process(osi)


class Bidirectional(SectionBase):
    """
    The Bidirectional Section Class
    
    This command allows the user to construct a Bidirectional section, which is a stress-resultant plasticity model of
    two coupled forces. The yield surface is circular and there is combined isotropic and kinematic hardening.
    """
    op_type = 'Bidirectional'

    def __init__(self, osi, e_mod, fy, hiso, hkin, code1='Vy', code2='P'):
        """
        Initial method for Bidirectional

        Parameters
        ----------
        e_mod: float
            Elastic modulus
        fy: float
            Yield force
        hiso: float
            Isotropic hardening modulus
        hkin: float
            Kinematic hardening modulus
        code1: str
            Section force code for direction 1 (optional)
        code2: str
            Section force code for direction 2 (optional) one of the following section code may be used: * ``'p'`` axial
            force-deformation * ``'mz'`` moment-curvature about section local z-axis * ``'vy'`` shear force-deformation along
            section local y-axis * ``'my'`` moment-curvature about section local y-axis * ``'vz'`` shear force-deformation
            along section local z-axis * ``'t'`` torsion force-deformation
        """
        self.e_mod = float(e_mod)
        self.fy = float(fy)
        self.hiso = float(hiso)
        self.hkin = float(hkin)
        self.code1 = code1
        self.code2 = code2
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.e_mod, self.fy, self.hiso, self.hkin, self.code1, self.code2]
        self.to_process(osi)


class Isolator2spring(SectionBase):
    """
    The Isolator2spring Section Class
    
    This command is used to construct an Isolator2spring section object, which represents the buckling behavior of an
    elastomeric bearing for two-dimensional analysis in the lateral and vertical plane. An Isolator2spring section
    represents the resultant force-deformation behavior of the bearing, and should be used with a
    zeroLengthSection element. The bearing should be constrained against rotation.
    """
    op_type = 'Isolator2spring'

    def __init__(self, osi, tol, k1, fyo, k2o, kvo, hb, pe, po=0.0):
        """
        Initial method for Isolator2spring

        Parameters
        ----------
        tol: float
            Tolerance for convergence of the element state. suggested value: e-12 to e-10. opensees will warn if
            convergence is not achieved, however this usually does not prevent global convergence.
        k1: float
            Initial stiffness for lateral force-deformation
        fyo: float
            Nominal yield strength for lateral force-deformation
        k2o: float
            Nominal postyield stiffness for lateral force-deformation
        kvo: float
            Nominal stiffness in the vertical direction
        hb: float
            Total height of elastomeric bearing
        pe: float
            Euler buckling load for the bearing
        po: float
            Axial load at which nominal yield strength is achieved (optional)
        """
        self.tol = float(tol)
        self.k1 = float(k1)
        self.fyo = float(fyo)
        self.k2o = float(k2o)
        self.kvo = float(kvo)
        self.hb = float(hb)
        self.pe = float(pe)
        self.po = float(po)
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.tol, self.k1, self.fyo, self.k2o, self.kvo, self.hb, self.pe, self.po]
        self.to_process(osi)


class LayeredShell(SectionBase):
    """
    The LayeredShell Section Class

    This command will create the section of the multi-layer shell element, including the multi-dimensional concrete,
    reinforcement material and the corresponding thickness.
    """
    op_type = 'LayeredShell'

    def __init__(self, osi, mats):
        """
        Initial method for LayeredShell

        Parameters
        ----------
        mats: list
            A list of material objs and thickness, ``[[mat1,thk1], ..., [mat2,thk2]]``
        """
        self.mats = []
        for i, mat in enumerate(mats):
            # self.mats.append([mats[i][0].tag, mats[i][1]])
            self.mats.append(mats[i][0].tag)
            self.mats.append(mats[i][1])

        self.n_layers = int(len(self.mats))
        osi.n_sect += 1
        self._tag = osi.n_sect
        self._parameters = [self.op_type, self._tag, self.n_layers, *self.mats]
        self.to_process(osi)
